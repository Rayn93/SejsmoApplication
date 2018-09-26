from django.urls import path

from .views import StatisticView, GutenbergRichterView, QuakeMapView

urlpatterns = [
    path('', StatisticView.as_view(), name='statistic'),
    path('rozklad-gutenberga-richtera', GutenbergRichterView.as_view(), name='gutenberg-richter'),
    path('mapa', QuakeMapView.as_view(), name='quake-map'),
]