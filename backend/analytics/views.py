from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from django.db.models import Sum, Count, Avg
from django.utils import timezone
from datetime import timedelta, date
from .models import PageView, ProductEngagement, DailyStats
from .serializers import PageViewSerializer, ProductEngagementSerializer, DailyStatsSerializer


class TrackView(APIView):
    """Single endpoint to receive all tracking events from the frontend."""
    permission_classes = [AllowAny]

    def post(self, request):
        event = request.data.get('event')
        session_id = request.data.get('session_id', 'anonymous')
        today = timezone.now().date()

        if event == 'page_view':
            PageView.objects.create(
                session_id=session_id,
                page=request.data.get('page', 'home'),
                category_key=request.data.get('category_key', ''),
                product_id=request.data.get('product_id', ''),
                product_name=request.data.get('product_name', ''),
                referrer=request.data.get('referrer', ''),
            )
            stats, _ = DailyStats.objects.get_or_create(date=today)
            stats.page_views += 1
            if request.data.get('is_new_session'):
                stats.sessions += 1
            if request.data.get('page') == 'checkout':
                stats.checkouts += 1
            stats.save()

        elif event == 'product_time':
            time_ms = int(request.data.get('time_spent_ms', 0))
            if time_ms > 0:
                ProductEngagement.objects.create(
                    session_id=session_id,
                    product_id=request.data.get('product_id', ''),
                    product_name=request.data.get('product_name', ''),
                    category_key=request.data.get('category_key', ''),
                    time_spent_ms=time_ms,
                )

        return Response({'ok': True})


class DashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        today = timezone.now().date()
        thirty_days_ago = today - timedelta(days=30)

        # Daily stats for last 30 days
        daily = DailyStats.objects.filter(date__gte=thirty_days_ago).order_by('date')
        daily_data = {str(d.date): {'sessions': d.sessions, 'page_views': d.page_views, 'checkouts': d.checkouts} for d in daily}

        # Page view breakdown
        page_totals = (
            PageView.objects.values('page')
            .annotate(count=Count('id'))
            .order_by('-count')
        )

        # Top products by views
        top_products = (
            PageView.objects.filter(page='product')
            .exclude(product_id='')
            .values('product_id', 'product_name')
            .annotate(views=Count('id'))
            .order_by('-views')[:10]
        )

        # Top products by time spent
        top_by_time = (
            ProductEngagement.objects
            .values('product_id', 'product_name')
            .annotate(total_ms=Sum('time_spent_ms'), sessions=Count('id'))
            .order_by('-total_ms')[:10]
        )

        # Category views
        cat_views = (
            PageView.objects.filter(page='category')
            .exclude(category_key='')
            .values('category_key')
            .annotate(views=Count('id'))
            .order_by('-views')
        )

        # Summary totals
        total_sessions = DailyStats.objects.aggregate(t=Sum('sessions'))['t'] or 0
        total_checkouts = DailyStats.objects.aggregate(t=Sum('checkouts'))['t'] or 0
        total_pv = PageView.objects.count()

        return Response({
            'summary': {
                'total_sessions': total_sessions,
                'total_page_views': total_pv,
                'total_checkouts': total_checkouts,
                'conversion_rate': round(total_checkouts / max(total_sessions, 1) * 100, 1),
            },
            'daily': daily_data,
            'page_views': list(page_totals),
            'top_products_by_views': list(top_products),
            'top_products_by_time': list(top_by_time),
            'category_views': list(cat_views),
        })
