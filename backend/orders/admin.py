from django.contrib import admin
from .models import Order, OrderItem, CategoryDiscount, ProductDiscount


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_id', 'product_name', 'quantity', 'unit_price', 'discount_pct', 'line_total']
    can_delete = False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer_name', 'customer_phone', 'total', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    list_editable = ['status']
    search_fields = ['order_number', 'customer_name', 'customer_phone', 'customer_email']
    readonly_fields = ['order_number', 'subtotal', 'discount_amount', 'shipping_charge', 'total', 'created_at']
    inlines = [OrderItemInline]
    ordering = ['-created_at']


@admin.register(CategoryDiscount)
class CategoryDiscountAdmin(admin.ModelAdmin):
    list_display = ['category_key', 'min_qty', 'discount_pct', 'is_active']
    list_editable = ['discount_pct', 'is_active']
    ordering = ['category_key', 'min_qty']


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'min_qty', 'discount_pct', 'is_active']
    list_editable = ['discount_pct', 'is_active']
    ordering = ['product_id', 'min_qty']
