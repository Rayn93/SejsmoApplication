import django_tables2 as tables
from django_tables2.utils import A
from .models import LocalQuake
from django.utils.safestring import mark_safe
from django.urls import reverse


class LocalQuakesTable(tables.Table):
    more_link = tables.LinkColumn('localQuakes:detail', text='Więcej', args=[A('pk')], orderable=False, empty_values=(), verbose_name='Więcej')

    class Meta:
        model = LocalQuake
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'city', 'magnitude', 'eventDate')
        attrs = {"class": "table table-bordered"}


    def render_more_link(self,record):
        return mark_safe('<a href=' + reverse("localQuakes:detail", args=[record.pk]) + ' class ="btn btn-primary"><span class ="glyphicon glyphicon-edit"></span></a>')




