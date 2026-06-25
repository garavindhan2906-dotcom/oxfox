from django.db import models


class Category(models.Model):
    key = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, default='📦')
    description = models.TextField(blank=True)
    filters = models.JSONField(default=list, help_text='List of filter tag strings')
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.icon} {self.name}'


class Product(models.Model):
    BADGE_NONE = ''
    BADGE_BEST = 'best'
    BADGE_NEW = 'new'
    BADGE_CHOICES = [
        (BADGE_NONE, 'None'),
        (BADGE_BEST, 'Bestseller'),
        (BADGE_NEW, 'New Arrival'),
    ]

    product_id = models.CharField(max_length=60, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    emoji = models.CharField(max_length=10, default='📦')
    price = models.PositiveIntegerField(help_text='Selling price in INR')
    mrp = models.PositiveIntegerField(help_text='Maximum retail price in INR')
    material = models.CharField(max_length=100, default='Silicone')
    badge = models.CharField(max_length=10, choices=BADGE_CHOICES, blank=True, default='')
    filter_tag = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    discount = models.PositiveSmallIntegerField(
        default=0, help_text='Individual product discount percentage (0 = no discount)'
    )
    is_active = models.BooleanField(default=True)
    is_custom = models.BooleanField(default=False, help_text='Added via admin panel')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category__order', 'name']

    def __str__(self):
        return f'{self.emoji} {self.name}'

    @property
    def primary_image(self):
        img = self.images.order_by('order').first()
        return img.url if img else ''

    @property
    def all_images(self):
        return list(self.images.order_by('order').values_list('url', flat=True))

    @property
    def final_price(self):
        if self.discount > 0:
            return round(self.mrp * (1 - self.discount / 100))
        return self.mrp


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    url = models.TextField()
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ['order']
        unique_together = ('product', 'order')

    def __str__(self):
        return f'{self.product.name} — image {self.order}'


class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=400, blank=True)
    cta_text = models.CharField(max_length=100, default='Shop Now')
    cta_link = models.CharField(max_length=200, default='#')
    cta_secondary_text = models.CharField(max_length=100, blank=True)
    cta_secondary_link = models.CharField(max_length=200, blank=True)
    bg_gradient = models.CharField(
        max_length=200,
        default='linear-gradient(135deg,#3D0808 0%,#6B1020 100%)',
    )
    text_color = models.CharField(max_length=20, default='#FFFFFF')
    accent_color = models.CharField(max_length=20, default='#FAE8E8')
    tag_text = models.CharField(max_length=100, blank=True)
    deco_emoji = models.CharField(max_length=10, blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
