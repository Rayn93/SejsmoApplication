from django.shortcuts import render
from stations.models import Station
from localQuakes.models import LocalQuake

# Create your views here.
from django.views.generic import TemplateView, ListView


class HomeView(ListView):
    template_name = "pages/home.html"

    queryset = LocalQuake.objects.all().order_by('-id')[:5]
    context_object_name = 'last_quakes'



class AboutView(ListView):
    template_name = "pages/about.html"
    model = Station

