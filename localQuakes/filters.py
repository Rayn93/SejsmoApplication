from .models import LocalQuake
import django_filters

class QuakeFilter(django_filters.FilterSet):
    eventDate_gt = django_filters.DateFilter(field_name='eventDate', lookup_expr='year__gt', label='hej')
    eventDate_lt = django_filters.DateFilter(field_name='eventDate', lookup_expr='year__lt')
    date_range = django_filters.DateRangeFilter(field_name='eventDate')

    class Meta:
        model = LocalQuake
        fields = ['city', 'eventDate', 'magnitude', ]