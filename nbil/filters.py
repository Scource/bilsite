import django_filters
from django import forms
from .models import UR_objects, UR_conn


class URFilter(django_filters.FilterSet):
	name=django_filters.CharFilter(lookup_expr='icontains')
	code=django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = UR_objects
		fields = ['name', 'code',]


class ConnFilter(django_filters.FilterSet):
	POB = forms.ModelChoiceField(queryset=UR_objects.objects.filter(name='qweqweq'), to_field_name = 'code')
	#POB = forms.ModelChoiceField(queryset=UR_objects.objects.filter(is_pob=0), to_field_name = 'name')
	SE = forms.ModelChoiceField(queryset=UR_objects.objects.filter(is_pob=1), to_field_name = 'name')
	class Meta:
		model = UR_conn
		fields = {'POB':['exact',],

		'DT_from': ['range'],
		}