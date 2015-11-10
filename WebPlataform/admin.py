from django.contrib import admin

# Register your models here.
from .models import Paciente, Medico, RegistroEEG


class PacientesAdmin(admin.ModelAdmin):
    fields = ['docId', 'nombre_completo', 'historia_clinica', 'EPS']
    list_display = ('docId', 'nombre_completo', 'historia_clinica', 'EPS')


class MedicosAdmin(admin.ModelAdmin):
    fields = ['nombre_completo', 'docId', 'EPS']
    list_display = ('nombre_completo', 'docId', 'EPS')

admin.site.register(Paciente, PacientesAdmin)
admin.site.register(Medico, MedicosAdmin)
admin.site.register(RegistroEEG)

