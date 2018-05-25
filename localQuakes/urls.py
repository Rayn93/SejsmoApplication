from django.urls import path

# from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='localQuakes/localQuakesList.html'), name='localCatalog'),
    path('wstrzas-lokalny', TemplateView.as_view(template_name='localQuakes/localQuakeDetail.html'), name='localEvent'),
]