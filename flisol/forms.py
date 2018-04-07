from django import forms


# from registry.models import Person


class PersonForm(forms.Form):
	# pass

	# class Meta:
	# 	model = Person
	# 	fields = "__all__"

	name = forms.CharField(
		max_length=200,
		required=True
	)
	occupation = forms.CharField(
		max_length=100,
		required=False
	)
	institution = forms.CharField(
		max_length=100,
		required=False
	)
	email = forms.EmailField(
		max_length=200,
		required=True
	)
	phone = forms.CharField(
		max_length=20,
		required=False
	)
	subject = forms.CharField(
		max_length=500,
		required=False
	)
	requirements = forms.CharField(
		max_length=500,
		required=False
	)
