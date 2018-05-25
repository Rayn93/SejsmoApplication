from django.urls import path

# from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    path('o-projekcie', TemplateView.as_view(template_name='pages/about.html'), name='about'),
]