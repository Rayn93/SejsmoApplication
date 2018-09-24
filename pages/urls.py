from django.urls import path

from .views import HomeView, AboutView, ChartData

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('o-projekcie', AboutView.as_view(), name='about'),
    path('api/chart/data/', ChartData.as_view(), name='api-chart-data'),
]