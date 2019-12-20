from django import forms
from .models import UR_objects

class Conn_form(forms.ModelForm):
	class Meta:
		model = UR_objects
		exclude = ['user_id']

class edit_form(forms.ModelForm):
	class Meta:
		model=UR_objects
		exclude = ['user_id']