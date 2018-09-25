import plotly.offline as opy
import plotly.graph_objs as go

import collections


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


class StatisticView(TemplateView):
    template_name = "pages/statistic.html"



class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        dates = [LocalQuake.magnitude for LocalQuake in LocalQuake.objects.all()]

        # dates = [log10(element) for element in dates]

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


class Graph(TemplateView):
    template_name = 'pages/graph.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)

        # x = [-2, 0, 4, 6, 7]
        # y = [q**2-q+3 for q in x]
        #
        # x2 = [-1, 3, 4, 1, 2]
        # y2 = [q ** 3 - q + 5 for q in x]


        # trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10},
        #                     mode="lines",  name='1st Trace')
        #
        # trace2 = go.Scatter(x=x2, y=y2, marker={'color': 'red', 'symbol': 104, 'size': 10},
        #                     mode="lines", name='2st Trace')



        # data=go.Data([trace1])
        # layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
        # figure=go.Figure(data=data,layout=layout)
        # div = opy.plot(figure, auto_open=False, output_type='div')
        #
        # data2 = go.Data([trace2])
        # layout = go.Layout(title="Meine Daten", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        # figure2 = go.Figure(data=data2, layout=layout)
        # div2 = opy.plot(figure2, auto_open=False, output_type='div')

        # allMagnitudes = [LocalQuake.magnitude for LocalQuake in LocalQuake.objects.all()]
        # # sortedMagnitudes = sorted(allMagnitudes, key=lambda student: student[0])
        # counter = collections.Counter(allMagnitudes)
        #
        #
        # context['graph'] = counter

        allMagnitudes = [LocalQuake.magnitude for LocalQuake in LocalQuake.objects.all()]
        allMagnitudesFloat = [float(i) for i in allMagnitudes]
        counter = collections.Counter(allMagnitudesFloat)
        x = [float(i) for i in counter.keys()]
        y = [float(i) for i in counter.values()]

        logy = [log10(element) for element in y]

        # od = collections.OrderedDict(sorted(counter.items()))

        # sortedMagnitudes = sorted(counter.items())

        data = [go.Bar(
            x=x,
            y=logy
        )]
        layout = go.Layout(title="Meine Daten", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        figure3 = go.Figure(data=data, layout=layout)
        div3 = opy.plot(figure3, auto_open=False, output_type='div')






        # # trace3 = go.Histogram(x=allMagnitudes, y=counter, cumulative=dict(enabled=True, direction='decreasing'))
        # trace3 = go.Histogram(x=allMagnitudesFloat)
        #
        #
        # data3 = go.Data([trace3])
        # layout = go.Layout(title="Meine Daten", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        # figure3 = go.Figure(data=data3, layout=layout)
        # div3 = opy.plot(figure3, auto_open=False, output_type='div')
        # #
        # context['graph'] = div
        # context['graph2'] = div2
        context['graph3'] = div3

        return context


