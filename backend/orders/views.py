from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Order, CategoryDiscount, ProductDiscount
from .serializers import OrderSerializer, CategoryDiscountSerializer, ProductDiscountSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'head', 'options']

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        if self.action == 'list' and self.request.user.is_staff:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all().prefetch_related('items')
        if user.is_authenticated:
            return Order.objects.filter(user=user).prefetch_related('items')
        session = self.request.query_params.get('session_id', '')
        return Order.objects.filter(session_id=session).prefetch_related('items')

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)


class CategoryDiscountListView(generics.ListAPIView):
    queryset = CategoryDiscount.objects.filter(is_active=True).order_by('category_key', 'min_qty')
    serializer_class = CategoryDiscountSerializer
    permission_classes = [AllowAny]


class CategoryDiscountAdminView(generics.ListCreateAPIView):
    queryset = CategoryDiscount.objects.all()
    serializer_class = CategoryDiscountSerializer
    permission_classes = [IsAdminUser]


class CategoryDiscountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryDiscount.objects.all()
    serializer_class = CategoryDiscountSerializer
    permission_classes = [IsAdminUser]


class ProductDiscountListView(generics.ListAPIView):
    queryset = ProductDiscount.objects.filter(is_active=True).order_by('product_id', 'min_qty')
    serializer_class = ProductDiscountSerializer
    permission_classes = [AllowAny]


class ProductDiscountAdminView(generics.ListCreateAPIView):
    queryset = ProductDiscount.objects.all()
    serializer_class = ProductDiscountSerializer
    permission_classes = [IsAdminUser]


class ProductDiscountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductDiscount.objects.all()
    serializer_class = ProductDiscountSerializer
    permission_classes = [IsAdminUser]
