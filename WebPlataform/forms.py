from django import forms

from.models import Paciente, Medico, RegistroEEG

__author__ = 'miltonarango'


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ["docId", "nombre_completo", "historia_clinica", "EPS"]

    def clean_docId(self):
        return self.cleaned_data.get("docId")


class RegistroEEGForm(forms.ModelForm):

    class Meta:
        model = RegistroEEG
        fields = ["paciente", "archivo_registro"]
    #registro = forms.FileField(label="Seleccione el archivo de registro", help_text="Formato .mat")


