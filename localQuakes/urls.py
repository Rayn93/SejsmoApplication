
from django.urls import path

# from . import views
from django.views.generic import TemplateView

from .views import LocalQuakesListView, LocalQuakeDetailView

urlpatterns = [
    path('', LocalQuakesListView.as_view(), name='list'),
    path('wstrzas-lokalny-id-<int:pk>/', LocalQuakeDetailView.as_view(), name='detail'),
]

