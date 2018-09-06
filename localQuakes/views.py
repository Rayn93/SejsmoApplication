from django.shortcuts import render
from .tables import LocalQuakesTable
from django_tables2 import RequestConfig

from .filters import QuakeFilter


# Create your views here.
from django.views.generic import ListView, DetailView

from .models import LocalQuake


# class LocalQuakesListView(ListView):
#     template_name = "localQuakes/localQuakesList.html"
#
#     # def get_queryset(self):
#     #     queryset = localQuake.objects.all()
#     #     return queryset
#
#     model = LocalQuake

def quakes_list(request):
    table = LocalQuake.objects.all()
    table_filter = QuakeFilter(request.GET, queryset=table)
    # RequestConfig(request).configure(table)
    return render(request, 'localQuakes/localQuakesList.html', {'filter': table_filter})




class LocalQuakeDetailView(DetailView):
    template_name = "localQuakes/localQuakeDetail.html"
    model = LocalQuake

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
