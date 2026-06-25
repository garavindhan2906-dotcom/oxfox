from rest_framework import serializers
from .models import PageView, ProductEngagement, DailyStats


class PageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageView
        fields = ['page', 'category_key', 'product_id', 'product_name', 'session_id', 'referrer']


class ProductEngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEngagement
        fields = ['product_id', 'product_name', 'category_key', 'time_spent_ms', 'session_id']


class DailyStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyStats
        fields = '__all__'
