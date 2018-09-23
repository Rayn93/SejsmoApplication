from django.shortcuts import render
from stations.models import Station
from localQuakes.models import LocalQuake

from globalQuakes.models import GlobalQuake

# Create your views here.
from django.views.generic import TemplateView, ListView


class HomeView(ListView):
    template_name = "pages/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     last_quakes = LocalQuake.objects.all().order_by('-id')[:5]
    #     last_earthquakes = GlobalQuake.objects.all().order_by('-id')[:5]
    #     context['group'] = zip(last_quakes, last_earthquakes)
    #     return context

    queryset = LocalQuake.objects.all().order_by('-id')[:20]
    context_object_name = 'last_quakes'

    # queryset2 = GlobalQuake.objects.all().order_by('-id')[:5]
    # context_object_name2 = 'last_earthquakes'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_earthquakes'] = GlobalQuake.objects.all().order_by('-id')[:10]
        return context


class AboutView(ListView):
    template_name = "pages/about.html"
    model = Station

