from django.shortcuts import render
from django.views.generic import FormView
from .forms import CForm


class CView(FormView):
	template_name = 'main.html'
