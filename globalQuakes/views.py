from django.shortcuts import render

from .filters import QuakeFilter
from django.views.generic import ListView, DetailView

from .models import GlobalQuake


def earthquakes_list(request):
    earthquakes_list = GlobalQuake.objects.all().order_by('-eventDate')
    table_filter = QuakeFilter(request.GET, queryset=earthquakes_list)
    # RequestConfig(request).configure(table)

    return render(request, 'globalQuakes/globalQuakesList.html', {'filter': table_filter})



class GlobalQuakeDetailView(DetailView):
    template_name = "globalQuakes/globalQuakeDetail.html"
    model = GlobalQuake

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

