
from django.urls import path

# from . import views
from django.views.generic import TemplateView

from .views import quakes_list

from .views import LocalQuakeDetailView

urlpatterns = [
    path('', quakes_list, name='list'),
    path('wstrzas-lokalny-id-<int:pk>/', LocalQuakeDetailView.as_view(), name='detail'),
]

