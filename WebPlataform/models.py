from django.db import models

# Create your models here.


class Paciente(models.Model):

    historia_clinica = models.CharField(max_length=120,  blank=True, null=True)
    docId = models.CharField(max_length=15, blank=False, null=False)
    nombre_completo = models.CharField(max_length=120,  blank=False, null=False)
    EPS = models.CharField(max_length=120,  blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    modificacion = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nombre_completo + ": " +self.docId


class Medico(models.Model):

    docId = models.CharField(max_length=15, blank=False, null=False)
    nombre_completo = models.CharField(max_length=120,  blank=False, null=False)
    EPS = models.CharField(max_length=120,  blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    modificacion = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "Dr. %s" % self.nombre_completo


class RegistroEEG(models.Model):

    fecha_registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    paciente = models.ForeignKey(Paciente)
    archivo_registro = models.FileField(upload_to="registrosEEG/Pacientes/")
    comentario = models.CharField(max_length=120,  blank=True, null=True)

    def __unicode__(self):
        return self.paciente.docId
