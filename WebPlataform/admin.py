from django.contrib import admin

# Register your models here.
from .models import Paciente, Medico, RegistroEEG

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(RegistroEEG)
