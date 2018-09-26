from django.urls import path

from .views import HomeView, AboutView, contactView, successView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('o-projekcie', AboutView.as_view(), name='about'),
    path('kontakt', contactView, name='contact'),
    path('success', successView, name='success'),
]