from django.db import models

# Create your models here.


class Person(models.Model):

	name = models.CharField(
		verbose_name="Nombre Completo",
		max_length=200,
		blank=False,
		null=False
	)
	occupation = models.CharField(
		verbose_name="Ocupación / Profesión",
		max_length=100
	)
	institution = models.CharField(
		verbose_name="Institución",
		max_length=100
	)
	email = models.EmailField(
		verbose_name="Correo Electrónico",
		max_length=200,
		blank=False,
		null=False
	)
	phone = models.CharField(
		verbose_name="Teléfono / Celular",
		max_length=20,
		blank=True,
		null=True
	)
	subject = models.CharField(
		verbose_name="Tema",
		max_length=500,
		blank=True,
		null=True
	)
	requirements = models.CharField(
		verbose_name="Requerimientos Extras",
		max_length=500,
		blank=True,
		null=True
	)
