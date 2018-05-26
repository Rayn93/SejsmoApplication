from django.shortcuts import render
from stations.models import station

# Create your views here.
from django.views.generic import TemplateView, ListView


class HomeView(TemplateView):
    template_name = "home.html"



class AboutView(ListView):
    template_name = "pages/about.html"

    model = station

