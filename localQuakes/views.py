from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import LocalQuake


class LocalQuakesListView(ListView):
    template_name = "localQuakes/localQuakesList.html"

    # def get_queryset(self):
    #     queryset = localQuake.objects.all()
    #     return queryset

    model = LocalQuake


class LocalQuakeDetailView(DetailView):
    template_name = "localQuakes/localQuakeDetail.html"
    model = LocalQuake

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
