from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from .models import Station


class StationDetailView(DetailView):
    template_name = "stations/stationDetail.html"
    model = Station

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
