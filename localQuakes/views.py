from django.shortcuts import render
from .tables import LocalQuakesTable
from django_tables2 import RequestConfig

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

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
    table = LocalQuakesTable(LocalQuake.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'localQuakes/localQuakesList.html', {'localQuakes': table})




class LocalQuakeDetailView(DetailView):
    template_name = "localQuakes/localQuakeDetail.html"
    model = LocalQuake

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
