from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet, CategoryDiscountListView, CategoryDiscountAdminView, CategoryDiscountDetailView,
    ProductDiscountListView, ProductDiscountAdminView, ProductDiscountDetailView,
)

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('discounts/', CategoryDiscountListView.as_view(), name='discounts-list'),
    path('discounts/admin/', CategoryDiscountAdminView.as_view(), name='discounts-admin'),
    path('discounts/admin/<int:pk>/', CategoryDiscountDetailView.as_view(), name='discounts-admin-detail'),
    path('product-discounts/', ProductDiscountListView.as_view(), name='product-discounts-list'),
    path('product-discounts/admin/', ProductDiscountAdminView.as_view(), name='product-discounts-admin'),
    path('product-discounts/admin/<int:pk>/', ProductDiscountDetailView.as_view(), name='product-discounts-admin-detail'),
]
