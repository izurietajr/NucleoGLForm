
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView

from flisol.forms import PersonForm


class PersonView(CreateView):
	form_class = PersonForm
	template_name = 'person/registry.html'
	success_url = reverse_lazy('flisol:thank_you')


class ThankYouView(TemplateView):
	template_name = 'person/thank_you.html'