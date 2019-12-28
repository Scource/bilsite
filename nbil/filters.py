import django_filters
from django import forms
from .models import UR_objects, UR_conn


class URFilter(django_filters.FilterSet):
    class Meta:
        model = UR_objects
        fields = ['name', 'code',]


class ConnFilter(django_filters.FilterSet):
	POB = forms.ModelChoiceField(queryset=UR_objects.objects.filter(is_pob=0), to_field_name = 'name')
	SE = forms.ModelChoiceField(queryset=UR_objects.objects.filter(is_pob=1), to_field_name = 'name')
	class Meta:
		model = UR_conn
		fields = ['POB', 'SE',]