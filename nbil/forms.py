from django import forms
from .models import UR_objects, UR_conn, tariff_data


class Conn_form(forms.ModelForm):

	POB = forms.ModelChoiceField(queryset=UR_objects.objects.filter(is_pob=0), to_field_name = 'name')
	SE = forms.ModelChoiceField(queryset=UR_objects.objects.filter(is_pob=1), to_field_name = 'name')
	DT_to = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
	class Meta:
		model = UR_conn
		exclude = ['user_id']
		#'DT_to' = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))

class UR_edit_form(forms.ModelForm):
	class Meta:
		model=UR_objects
		exclude = ['user_id']


class UR_form_create(forms.ModelForm):
	class Meta:
		model=UR_objects
		fields = ['code', 'name', 'is_pob']


class conn_edit_form(forms.ModelForm):

	#POB = forms.ModelChoiceField(queryset=UR_objects.objects.filter(id=1), to_field_name = 'name')
	#SE = forms.ModelChoiceField(queryset=UR_objects.objects.filter(is_pob=1), to_field_name = 'code')
	
	class Meta:
		model=UR_conn
		fields = ['POB', 'SE', 'DT_from', 'DT_to']


class UploadFileForm(forms.Form):
	file = forms.FileField()