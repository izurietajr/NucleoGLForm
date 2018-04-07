from django.contrib import admin

# Register your models here.
from flisol.models import Person


@admin.register(Person)
class AuthorAdmin(admin.ModelAdmin):
    pass