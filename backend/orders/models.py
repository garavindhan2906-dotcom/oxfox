from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_PROCESSING = 'processing'
    STATUS_SHIPPED = 'shipped'
    STATUS_DELIVERED = 'delivered'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_SHIPPED, 'Shipped'),
        (STATUS_DELIVERED, 'Delivered'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    session_id = models.CharField(max_length=64, blank=True, db_index=True)
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)

    # Shipping details
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=254, blank=True)
    customer_phone = models.CharField(max_length=15)
    shipping_address = models.TextField()
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)

    # Pricing
    subtotal = models.PositiveIntegerField(default=0)
    discount_amount = models.PositiveIntegerField(default=0)
    shipping_charge = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    first_order_discount_pct = models.PositiveSmallIntegerField(default=0)

    # Payment
    payment_method = models.CharField(max_length=20, default='cod')

    # Notes
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order {self.order_number} — ₹{self.total}'

    def save(self, *args, **kwargs):
        if not self.order_number:
            import random, string
            prefix = 'OXF'
            suffix = ''.join(random.choices(string.digits, k=6))
            self.order_number = f'{prefix}{suffix}'
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_id = models.CharField(max_length=60)
    product_name = models.CharField(max_length=200)
    category_key = models.CharField(max_length=50, blank=True)
    emoji = models.CharField(max_length=10, default='📦')
    image_url = models.CharField(max_length=500, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    unit_price = models.PositiveIntegerField()
    discount_pct = models.PositiveSmallIntegerField(default=0)
    line_total = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity}x {self.product_name}'

    def save(self, *args, **kwargs):
        if not self.line_total:
            discounted = round(self.unit_price * (1 - self.discount_pct / 100))
            self.line_total = discounted * self.quantity
        super().save(*args, **kwargs)


class CategoryDiscount(models.Model):
    """Tiered category-level discounts controlled by admin."""
    category_key = models.CharField(max_length=50, db_index=True)
    min_qty = models.PositiveSmallIntegerField()
    discount_pct = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['category_key', 'min_qty']
        unique_together = ('category_key', 'min_qty')

    def __str__(self):
        return f'{self.category_key}: {self.min_qty}+ → {self.discount_pct}% off'


class ProductDiscount(models.Model):
    """Per-product quantity-tiered discounts set by admin."""
    product_id = models.CharField(max_length=60, db_index=True)
    min_qty = models.PositiveSmallIntegerField()
    discount_pct = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['product_id', 'min_qty']
        unique_together = ('product_id', 'min_qty')

    def __str__(self):
        return f'{self.product_id}: {self.min_qty}+ units → {self.discount_pct}% off'
