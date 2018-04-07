
from django.contrib import admin

from flisol.models import Person


@admin.register(Person)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'phone')
    # pass