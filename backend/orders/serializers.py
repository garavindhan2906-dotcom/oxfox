from rest_framework import serializers
from .models import Order, OrderItem, CategoryDiscount, ProductDiscount


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product_id', 'product_name', 'category_key', 'emoji', 'image_url',
                  'quantity', 'unit_price', 'discount_pct', 'line_total']
        read_only_fields = ['line_total']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'status', 'session_id', 'customer_name', 'customer_email',
            'customer_phone', 'shipping_address', 'city', 'state', 'pincode',
            'subtotal', 'discount_amount', 'shipping_charge', 'total', 'payment_method',
            'first_order_discount_pct', 'notes', 'items', 'created_at',
        ]
        read_only_fields = ['id', 'order_number', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            item_data.pop('line_total', None)
            discounted = round(item_data['unit_price'] * (1 - item_data.get('discount_pct', 0) / 100))
            item_data['line_total'] = discounted * item_data['quantity']
            OrderItem.objects.create(order=order, **item_data)
        # Recalculate totals
        subtotal = sum(i.line_total for i in order.items.all())
        shipping = 0 if subtotal >= 5000 else 99
        disc_amt = round(subtotal * validated_data.get('first_order_discount_pct', 0) / 100)
        order.subtotal = subtotal
        order.shipping_charge = shipping
        order.discount_amount = disc_amt
        order.total = subtotal - disc_amt + shipping
        order.save()
        return order


class CategoryDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDiscount
        fields = '__all__'


class ProductDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDiscount
        fields = '__all__'
