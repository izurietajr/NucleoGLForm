from django.forms import forms

from form.models import Person


class PersonForm(forms.Form):
	class Meta:
		model = Person
		fields = "__all__"
