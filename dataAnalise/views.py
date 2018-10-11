from django.shortcuts import render

import plotly.offline as opy
import plotly.graph_objs as go

import operator
import collections
from itertools import accumulate
import statistics
import math

from django.views.generic import TemplateView, ListView
from localQuakes.models import LocalQuake

from dataAnalise.forms import InputDataForAnalysis

from django.db.models.functions import TruncMonth
from django.db.models import Count


class StatisticView(TemplateView):
    template_name = "statistic.html"

    # allMonths = LocalQuake.objects.annotate(month=TruncMonth('timestamp')).values('month').annotate(c=Count('id')).values('month', 'c')

    def get_context_data(self, **kwargs):
        context = super(StatisticView, self).get_context_data(**kwargs)

        allMagnitudes = [LocalQuake.magnitude for LocalQuake in LocalQuake.objects.all()]
        allCities = [LocalQuake.city for LocalQuake in LocalQuake.objects.all()]
        allMonths = [LocalQuake.eventDate for LocalQuake in LocalQuake.objects.all()]

        timeRange = subList(allMonths)
        avgTimeRange = statistics.mean(timeRange)


        context['histogramMag'] = renderHistogram(allMagnitudes, 'Histogram magnitud dla wstrząsów lokalnych', 'Magnituda lokalna ML', 'Częstość N')
        context['histogramCity'] = renderHistogram(allCities, 'Ilość wstrząsów w poszczególnych miastach', 'Miasto', 'Liczba wstrząsów')
        context['allMonths'] = renderHistogram(allMonths, 'Ilość wstrząsów w poszczególnych miesiącach', 'Miesiąc', 'Liczba wstrząsów', 20)
        context['timeRange'] = renderHistogram(timeRange, 'Histogram rozkładu odstępów czasowych', 'Czas [godziny]', 'Liczba wstrząsów', 80)
        context['avgTimeRange'] = float("{0:.2f}".format(avgTimeRange))

        return context


class QuakeMapView(TemplateView):
    template_name = "all-quakes-map.html"

    def get_context_data(self, **kwargs):
        context = super(QuakeMapView, self).get_context_data(**kwargs)
        context['last_quakes'] = LocalQuake.objects.all()
        return context



class GutenbergRichterView(TemplateView):
    template_name = 'gutenberg-richter.html'

    def get_context_data(self, **kwargs):
        context = super(GutenbergRichterView, self).get_context_data(**kwargs)

        allMagnitudes = [LocalQuake.magnitude for LocalQuake in LocalQuake.objects.all()]
        allMagnitudesFloat = [float(i) for i in allMagnitudes]
        counter = collections.Counter(allMagnitudesFloat)


        # Histogram normalny
        xnorlam = [float(i) for i in counter.keys()]
        ynormal = [float(i) for i in counter.values()]

        context['allMagnitudes'] = allMagnitudes
        context['histNormal'] = renderBarChart(xnorlam, ynormal, 'Histogram wstrząsów lokalnych', 'Magnituda lokalna ML', 'Częstość N')

        ##########################
        # Histogram zlogarytmowany

        logy = [math.log10(element) for element in ynormal]
        context['histLogy'] = renderBarChart(xnorlam, logy, 'Histogram wstrząsów lokalnych', 'Magnituda lokalna ML', 'Log(N)')

        ##########################
        # Histogram obcięty

        magMin = max(counter.items(), key=operator.itemgetter(1))[0]
        magMax = float("{0:.2f}".format(2*max(xnorlam) - sorted(xnorlam)[-2] ))

        cutCatalogMag = {k: v for k, v in counter.items() if k >= magMin}

        orderDict = collections.OrderedDict(sorted(cutCatalogMag.items()))
        sortcutCatalogMag = dict(orderDict)

        xCut = [float(i) for i in sortcutCatalogMag.keys()]
        yCut = [float(i) for i in sortcutCatalogMag.values()]

        yCut = list(map(int, yCut))
        logyCut = [math.log10(element) for element in yCut]

        context['histCut'] = renderBarChart(xCut, logyCut, 'Obcięty histogram wstrząsów lokalnych', 'Magnituda lokalna ML', 'Log(N)')
        context['magMin'] = magMin
        context['magMax'] = magMax


        ##########################
        # Wykres Logy skumulowany

        yCumulative = list(accumulate((yCut[::-1])))[::-1]
        logyCumulative = [math.log10(element) for element in yCumulative]


        ##########################
        # Metoda największej wiarygodności

        cutMagnitudeList = [i for i in allMagnitudesFloat if i >= magMin]

        magAvg = statistics.mean(cutMagnitudeList)
        magStaDev = statistics.stdev(xCut)
        b = math.log10(math.e) / (magAvg - magMin)
        delb = 2.3 * b ** 2 * magStaDev

        a = []
        for y, x in zip(logyCumulative, xCut):
            z = y + (b*x)
            a.append(z)

        aAvg = statistics.mean(a)
        dela = statistics.stdev(a)

        regliny = []
        for x in xCut:
            z = aAvg + (-b*x)
            regliny.append(z)

        dataCumulative = [go.Bar(
            x=xCut,
            y=logyCumulative,
            marker=dict(
                color='#00a651'
            ),
            name='Skumulowana liczba wstrząsów Nsk'
        ), go.Scatter(
            x=xCut,
            y=regliny,
            marker=dict(
                color='blue'
            ),
            name='Dopasowana linia metodą największej wiarygodności',

        )]

        layoutCumulative = go.Layout(title="Wykres dla N będących skumulowaną liczbą wstrząsów [Nsk] ",
                                     xaxis={'title': 'Magnituda lokalna ML'},
                                     yaxis={'title': 'Log(Nsk)'},
                                     )
        figureCumulative = go.Figure(data=dataCumulative, layout=layoutCumulative)
        divCumulative = opy.plot(figureCumulative, auto_open=False, output_type='div')
        context['chartRegLine'] = divCumulative


        context['magAvg'] = float("{0:.3f}".format(magAvg))
        context['magStaDev'] = float("{0:.3f}".format(magStaDev))
        context['b'] = float("{0:.3f}".format(b))
        context['delb'] = float("{0:.3f}".format(delb))
        context['a'] = float("{0:.3f}".format(aAvg))
        context['dela'] = float("{0:.3f}".format(dela))
        return context


class HazardView(TemplateView):
    template_name = 'hazard.html'


    def get(self, request):
        form = InputDataForAnalysis()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InputDataForAnalysis(request.POST)


        if form.is_valid():
            deltaT = form.cleaned_data['deltaT']
            mth = form.cleaned_data['mth']


        gutRich = GutenbergRichterView().get_context_data()
        btrue = gutRich['b']
        magMin = gutRich['magMin']
        beta = float("{0:.2f}".format(btrue/math.log10(math.e)))
        mthList = [x * 0.02 for x in range(0, 251)] #[0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
        mylambda = len(gutRich['allMagnitudes'])/18

        probabilityList = []
        timeList = []
        probabilityOfMth = float("{0:.2f}".format((1 - math.exp(-(mylambda)*deltaT*math.exp(-beta*(mth-magMin))))*100)) #poprawić lambdę
        timeOfMth = float("{0:.2f}".format(1/((mylambda)*math.exp(-beta*(mth-magMin)))*30))

        for m in mthList:
            r = 1 - math.exp(-(mylambda)*deltaT*math.exp(-beta*(m-magMin))) #poprawić lambdę
            t = 1/((mylambda)*math.exp(-beta*(m-magMin)))*30
            probabilityList.append(r)
            timeList.append(t)



        divProbability =renderScatterChart(mthList, probabilityList, "Prawdopodobieństwo przewyższenia magnitudy dla zadanego przedziału czasu", "Magnituda", "Prawdopodobieństwo")
        divTime = renderScatterChart(mthList, timeList, "Średni czas wystąpienia wstrząsu o danej magnitudzie", "Magnituda", "Czas (w dniach)")

        args = {'form': form, 'deltaT': deltaT, 'mth': mth, 'b': btrue, 'beta': beta, 'magMin': magMin, 'mylambda': mylambda,  'timeOfMth': timeOfMth, 'probabilityOfMth': probabilityOfMth,  'probabilityPlot': divProbability, 'timePlot': divTime}
        return render(request, self.template_name, args)



def renderScatterChart(x, y, title, xtitle, ytitle):

    data = [go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=dict(
            color='#00a651'
        ),
    )]
    layout = go.Layout(title=title, xaxis={'title': xtitle}, yaxis={'title': ytitle})
    figure = go.Figure(data=data, layout=layout)
    div = opy.plot(figure, auto_open=False, output_type='div')

    return div



def renderBarChart(x, y, title, xtitle, ytitle):

    data = [go.Bar(
        x=x,
        y=y,
        marker=dict(
            color='#00a651'
        ),
    )]
    layout = go.Layout(title=title, xaxis={'title': xtitle}, yaxis={'title': ytitle})
    figure = go.Figure(data=data, layout=layout)
    div = opy.plot(figure, auto_open=False, output_type='div')

    return div


def renderHistogram(x, title, xtitle, ytitle, nbins = 0):

    data = [go.Histogram(
        x=x,
        marker=dict(
            color='#00a651'
        ),
        nbinsx=nbins,

    )]
    layout = go.Layout(title=title, xaxis={'title': xtitle}, yaxis={'title': ytitle}, autosize=True, bargap=0.1)
    figure = go.Figure(data=data, layout=layout)
    div = opy.plot(figure, auto_open=False, output_type='div')

    return div


def subList(list):

    listWithRanges = []
    list = sorted(list)

    for index in range(len(list)):

        if index < len(list)-2:
            delTime = abs(list[index] - list[index+1])
            delDays = delTime.total_seconds()//3600

            if delDays < 400:
                listWithRanges.append(delDays)


    return listWithRanges

