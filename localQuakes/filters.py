from .models import LocalQuake
import django_filters
from django import forms

class QuakeFilter(django_filters.FilterSet):

    eventDate_gt = django_filters.DateFilter(field_name='eventDate', lookup_expr='gte', label='Od dnia')
    eventDate_lt = django_filters.DateFilter(field_name='eventDate', lookup_expr='lte', label='Do dnia')
    magnitude_gt = django_filters.NumberFilter(field_name='magnitude', lookup_expr='gte', label='Od magnitudy', widget=forms.NumberInput(attrs={'step': 0.1}))
    magnitude_lt = django_filters.NumberFilter(field_name='magnitude', lookup_expr='lte', label='Do magnitudy', widget=forms.NumberInput(attrs={'step': 0.1}))
    city = django_filters.CharFilter(lookup_expr='icontains', label='Miasto')

    date_range = django_filters.DateRangeFilter(field_name='eventDate', label='Okres czasu')

    class Meta:
        model = LocalQuake
        fields = ['city']