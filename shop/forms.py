from django import forms


class CForm(forms.Form):
	name = forms.CharField()
	