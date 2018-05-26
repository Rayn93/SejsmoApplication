from django.urls import path

# from . import views
from django.views.generic import TemplateView

from .views import HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('o-projekcie', AboutView.as_view(), name='about'),
]