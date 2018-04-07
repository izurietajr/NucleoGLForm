from django.shortcuts import render

from django.views.generic.edit import FormView

from form.forms import PersonForm


class PersonView(FormView):
	form_class = PersonForm
	# template_name =