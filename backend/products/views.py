from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from django.shortcuts import get_object_or_404
from .models import Category, Product, ProductImage, Banner
from .serializers import (
    CategorySerializer, CategoryListSerializer,
    ProductSerializer, ProductWriteSerializer, BannerSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True).prefetch_related('products__images')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'key']

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        return CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    @action(detail=True, methods=['get'], url_path='products')
    def products(self, request, pk=None):
        category = self.get_object()
        qs = category.products.filter(is_active=True)
        filter_tag = request.query_params.get('filter')
        if filter_tag and filter_tag != 'All':
            qs = qs.filter(filter_tag=filter_tag)
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True).select_related('category').prefetch_related('images')
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'material', 'filter_tag']
    ordering_fields = ['price', 'mrp', 'created_at', 'name']
    ordering = ['category__order', 'name']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductWriteSerializer
        return ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_queryset(self):
        qs = super().get_queryset()
        cat_key = self.request.query_params.get('category')
        filter_tag = self.request.query_params.get('filter')
        badge = self.request.query_params.get('badge')
        if cat_key:
            qs = qs.filter(category__key=cat_key)
        if filter_tag and filter_tag != 'All':
            qs = qs.filter(filter_tag=filter_tag)
        if badge:
            qs = qs.filter(badge=badge)
        return qs

    @action(detail=False, methods=['get'], url_path='new-arrivals')
    def new_arrivals(self, request):
        qs = self.get_queryset().filter(badge='new').order_by('-created_at')[:12]
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='bestsellers')
    def bestsellers(self, request):
        qs = self.get_queryset().filter(badge='best').order_by('-created_at')[:12]
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data)


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]
