import django_filters
from .models import UR_objects


class URFilter(django_filters.FilterSet):
    class Meta:
        model = UR_objects
        fields = ['name', 'code',]