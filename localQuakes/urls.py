
from django.urls import path

# from . import views
from django.views.generic import TemplateView

from .views import localQuakesListView, localQuakeDetailView

urlpatterns = [
    path('', localQuakesListView.as_view(), name='list'),
    path('wstrzas-lokalny-id-<int:pk>/', localQuakeDetailView.as_view(), name='detail'),
]

