from django.shortcuts import render
from stations.models import Station
from localQuakes.models import LocalQuake

from globalQuakes.models import GlobalQuake

# Create your views here.
from django.views.generic import TemplateView, ListView

from rest_framework.views import APIView
from rest_framework.response import Response

from math import *


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


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        dates = [LocalQuake.magnitude for LocalQuake in LocalQuake.objects.all()]

        dates = [log10(element) for element in dates]

        return Response(dates)

    # def get(self, request, format=None):
    #     magnitude = dict()
    #     for quake in LocalQuake.objects.all():
    #         magnitude[quake.eventDate] = quake.magnitude
    #
    #             # mag = sorted(mag.items(), key=lambda x: x[1])
    #         magnitude = dict(magnitude)
    #
    #     data = {
    #         "mag_date": magnitude.keys(),
    #         "mag_val": magnitude.values(),
    #     }
    #
    #     return Response(data)