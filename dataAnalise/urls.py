from django.urls import path

from .views import StatisticView, GutenbergRichterView, QuakeMapView, HazardView

urlpatterns = [
    path('', StatisticView.as_view(), name='statistic'),
    path('rozklad-gutenberga-richtera', GutenbergRichterView.as_view(), name='gutenberg-richter'),
    path('hazard-sejsmiczny', HazardView.as_view(), name='seismic-hazard'),
    path('mapa', QuakeMapView.as_view(), name='quake-map'),
]