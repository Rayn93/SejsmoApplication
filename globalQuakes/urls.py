
from django.urls import path

# from . import views
from django.views.generic import TemplateView

from .views import earthquakes_list

from .views import GlobalQuakeDetailView

urlpatterns = [
    path('', earthquakes_list, name='list'),
    path('trzesienie-id-<int:pk>/', GlobalQuakeDetailView.as_view(), name='detail'),
]

