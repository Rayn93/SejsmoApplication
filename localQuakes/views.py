from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from .models import localQuake


class localQuakesListView(ListView):
    template_name = "localQuakes/localQuakesList.html"

    # def get_queryset(self):
    #     queryset = localQuake.objects.all()
    #     return queryset

    model = localQuake


class localQuakeDetailView(TemplateView):
    template_name = "localQuakeDetail.html"
