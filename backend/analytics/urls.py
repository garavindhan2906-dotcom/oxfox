from django.urls import path
from .views import TrackView, DashboardView

urlpatterns = [
    path('track/', TrackView.as_view(), name='analytics-track'),
    path('dashboard/', DashboardView.as_view(), name='analytics-dashboard'),
]
