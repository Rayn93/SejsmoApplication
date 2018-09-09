from .models import LocalQuake
import django_filters

class QuakeFilter(django_filters.FilterSet):

    eventDate_gt = django_filters.DateFilter(field_name='eventDate', lookup_expr='gte', label='Od dnia')
    eventDate_lt = django_filters.DateFilter(field_name='eventDate', lookup_expr='lte', label='Do dnia')
    city = django_filters.CharFilter(lookup_expr='icontains', label='Miasto')

    date_range = django_filters.DateRangeFilter(field_name='eventDate', label='Przedział czasowy')

    class Meta:
        model = LocalQuake
        fields = ['city', 'magnitude']