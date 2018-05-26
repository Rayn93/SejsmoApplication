from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from .models import localQuake


class localQuakesListView(ListView):
    template_name = "localQuakes/localQuakesList.html"

    # def get_queryset(self):
    #     queryset = localQuake.objects.all()
    #     return queryset

    model = localQuake


class localQuakeDetailView(DetailView):
    template_name = "localQuakes/localQuakeDetail.html"

    model = localQuake

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
