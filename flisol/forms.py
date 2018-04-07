from django import forms


from flisol.models import Person


class PersonForm(forms.ModelForm):

	class Meta:
		model = Person
		exclude = []
