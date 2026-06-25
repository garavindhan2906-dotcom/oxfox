from django.db import models


class PageView(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('category', 'Category'),
        ('product', 'Product'),
        ('cart', 'Cart'),
        ('checkout', 'Checkout'),
        ('custom', 'Custom Order'),
        ('about', 'About Us'),
        ('search', 'Search'),
    ]

    session_id = models.CharField(max_length=64, db_index=True)
    page = models.CharField(max_length=20, choices=PAGE_CHOICES)
    category_key = models.CharField(max_length=50, blank=True)
    product_id = models.CharField(max_length=60, blank=True)
    product_name = models.CharField(max_length=200, blank=True)
    referrer = models.CharField(max_length=300, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.page} — {self.timestamp:%Y-%m-%d %H:%M}'


class ProductEngagement(models.Model):
    session_id = models.CharField(max_length=64, db_index=True)
    product_id = models.CharField(max_length=60, db_index=True)
    product_name = models.CharField(max_length=200, blank=True)
    category_key = models.CharField(max_length=50, blank=True)
    time_spent_ms = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.product_name} — {self.time_spent_ms}ms'


class DailyStats(models.Model):
    date = models.DateField(unique=True, db_index=True)
    sessions = models.PositiveIntegerField(default=0)
    page_views = models.PositiveIntegerField(default=0)
    checkouts = models.PositiveIntegerField(default=0)
    unique_products_viewed = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Daily Stats'

    def __str__(self):
        return f'{self.date} — {self.sessions} sessions'
