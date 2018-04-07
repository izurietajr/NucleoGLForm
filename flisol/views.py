
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView

from django.views.generic.edit import FormView

from flisol.forms import PersonForm


class PersonView(FormView):
	form_class = PersonForm
	template_name = 'person/personform.html'
	success_url = reverse_lazy('flisol:thank_you')

	def get_form(self, form_class=None):
		return self.form_class(data=self.request.POST)


class ThankYouView(TemplateView):
	template_name = 'person/thank_you.html'