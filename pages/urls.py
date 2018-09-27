from django.urls import path

from .views import HomeView, AboutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('o-projekcie', AboutView.as_view(), name='about'),
    path('kontakt', ContactView.as_view(), name='contact'),
]