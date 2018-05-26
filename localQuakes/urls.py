
from django.urls import path

# from . import views
from django.views.generic import TemplateView

from .views import localQuakesListView, localQuakeDetailView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='localQuakes/localQuakesList.html'), name='localCatalog'),
    path('', localQuakesListView.as_view(), name='localCatalog'),
    path('wstrzas-lokalny-<int:pk>/', localQuakeDetailView.as_view(), name='localEvent'),

]

