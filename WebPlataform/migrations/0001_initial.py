# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docId', models.CharField(max_length=15)),
                ('nombre_completo', models.CharField(max_length=120)),
                ('EPS', models.CharField(max_length=120, null=True, blank=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('historia_clinica', models.CharField(max_length=120, null=True, blank=True)),
                ('docId', models.CharField(max_length=15)),
                ('nombre_completo', models.CharField(max_length=120)),
                ('EPS', models.CharField(max_length=120, null=True, blank=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEEG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('archivo_registro', models.FileField(upload_to=b'/registrosEEG/Pacientes/')),
                ('paciente', models.ForeignKey(to='WebPlataform.Paciente')),
            ],
        ),
    ]
