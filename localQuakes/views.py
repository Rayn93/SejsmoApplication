from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class localQuakesListView(TemplateView):
    template_name = "localQuakesList.html"

class localQuakeDetailView(TemplateView):
    template_name = "localQuakeDetail.html"
