from django.urls import path

from .views import HomeView, AboutView, ChartData, StatisticView, Graph

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('o-projekcie', AboutView.as_view(), name='about'),
    path('statystyki', StatisticView.as_view(), name='statistic'),
    path('graph', Graph.as_view(), name='statistic'),
    path('api/chart/data/', ChartData.as_view(), name='api-chart-data'),
]