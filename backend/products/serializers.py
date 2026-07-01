from rest_framework import serializers
from .models import Category, Product, ProductImage, Banner


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['url', 'order']


class ProductSerializer(serializers.ModelSerializer):
    """Lightweight list serializer — no full images array to keep response small."""
    primary_image = serializers.ReadOnlyField()
    final_price = serializers.ReadOnlyField()
    category_key = serializers.CharField(source='category.key', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'product_id', 'category', 'category_key', 'category_name',
            'name', 'emoji', 'price', 'mrp', 'final_price', 'material',
            'badge', 'filter_tag', 'description', 'discount',
            'primary_image', 'is_active', 'is_custom',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProductDetailSerializer(ProductSerializer):
    """Full serializer with all images — used for single product retrieve."""
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['images']


class ProductWriteSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False, max_length=6
    )

    class Meta:
        model = Product
        fields = [
            'product_id', 'category', 'name', 'emoji', 'price', 'mrp',
            'material', 'badge', 'filter_tag', 'description', 'discount',
            'is_active', 'is_custom', 'images',
        ]

    def create(self, validated_data):
        image_urls = validated_data.pop('images', [])
        product = Product.objects.create(**validated_data)
        for i, url in enumerate(image_urls, start=1):
            if url:
                ProductImage.objects.create(product=product, url=url, order=i)
        return product

    def update(self, instance, validated_data):
        image_urls = validated_data.pop('images', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if image_urls is not None:
            instance.images.all().delete()
            for i, url in enumerate(image_urls, start=1):
                if url:
                    ProductImage.objects.create(product=instance, url=url, order=i)
        return instance


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'key', 'name', 'icon', 'description', 'filters', 'order', 'is_active', 'products', 'product_count']

    def get_product_count(self, obj):
        return obj.products.filter(is_active=True).count()


class CategoryListSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'key', 'name', 'icon', 'description', 'filters', 'order', 'is_active', 'product_count']

    def get_product_count(self, obj):
        return obj.products.filter(is_active=True).count()


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
