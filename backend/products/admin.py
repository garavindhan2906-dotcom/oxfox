from django.contrib import admin
from .models import Category, Product, ProductImage, Banner


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    max_num = 6
    fields = ['url', 'order']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'key', 'product_count', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'key']
    ordering = ['order']

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Products'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['emoji', 'name', 'category', 'price', 'mrp', 'badge', 'discount', 'is_active', 'is_custom']
    list_filter = ['category', 'badge', 'is_active', 'is_custom', 'material']
    list_editable = ['is_active', 'discount']
    search_fields = ['name', 'product_id', 'description']
    inlines = [ProductImageInline]
    fieldsets = (
        ('Basic Info', {
            'fields': ('product_id', 'category', 'name', 'emoji', 'material', 'filter_tag', 'badge')
        }),
        ('Pricing', {
            'fields': ('price', 'mrp', 'discount')
        }),
        ('Content', {
            'fields': ('description',)
        }),
        ('Status', {
            'fields': ('is_active', 'is_custom')
        }),
    )


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag_text', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'subtitle']
