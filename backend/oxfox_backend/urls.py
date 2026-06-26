from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework_simplejwt.views import TokenRefreshView
from pathlib import Path

# Website root — parent of backend/
SITE_ROOT = Path(settings.BASE_DIR).parent

def page(filename):
    """Serve an HTML page from the website root without Django template processing."""
    def view(request):
        return serve(request, filename, document_root=str(SITE_ROOT))
    return view

urlpatterns = [
    # ── Django built-in admin ──
    path('admin/', admin.site.urls),

    # ── Frontend pages ──
    path('', page('oxfox-studio.html'), name='home'),
    path('login/', page('oxfox-login.html'), name='login'),
    path('panel/', page('oxfox-admin.html'), name='panel'),

    # ── REST API ──
    path('api/auth/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ── Frontend static assets (Logo.png, oxfox-theme.css, images, etc.) ──
    re_path(r'^(?P<path>[\w.-]+\.(css|js|png|jpg|jpeg|gif|ico|svg|webp|woff2?|ttf))$',
            serve, {'document_root': str(SITE_ROOT)}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
