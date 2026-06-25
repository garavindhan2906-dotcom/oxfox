from django.contrib import admin
from .models import PageView, ProductEngagement, DailyStats


@admin.register(DailyStats)
class DailyStatsAdmin(admin.ModelAdmin):
    list_display = ['date', 'sessions', 'page_views', 'checkouts', 'unique_products_viewed']
    ordering = ['-date']
    readonly_fields = ['date', 'sessions', 'page_views', 'checkouts', 'unique_products_viewed']


@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ['page', 'product_name', 'category_key', 'session_id', 'timestamp']
    list_filter = ['page', 'timestamp']
    search_fields = ['product_name', 'category_key', 'session_id']
    readonly_fields = ['timestamp']
    ordering = ['-timestamp']


@admin.register(ProductEngagement)
class ProductEngagementAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'time_spent_ms', 'session_id', 'timestamp']
    search_fields = ['product_name', 'product_id']
    ordering = ['-timestamp']
