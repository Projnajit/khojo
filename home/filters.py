from dataclasses import field
import django_filters
from django_filters import CharFilter,NumberFilter
from .models import *

class Postfilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    rentfare = django_filters.NumberFilter(field_name='rentfare', lookup_expr='lte')
    bedroom = django_filters.NumberFilter(field_name='bedroom', lookup_expr='exact')
    bathroom = django_filters.NumberFilter(field_name='bathroom', lookup_expr='exact')
    location = CharFilter(field_name='location',lookup_expr='icontains')
    class Meta:
        model = Posts
        fields = ['location','bedroom']