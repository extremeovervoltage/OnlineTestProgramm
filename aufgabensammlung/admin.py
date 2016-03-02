from django.contrib import admin

from models import Simpleaufgabe, Aufgabensammlung, ErweiterterNutzer, Antwort
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(Simpleaufgabe)

admin.site.register(Aufgabensammlung)
admin.site.register(Antwort)


class ErweiterterNutzerInline(admin.StackedInline):
    model = ErweiterterNutzer
    can_delete = False
    verbose_name_plural = 'ErweiterteNutzer'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ErweiterterNutzerInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)