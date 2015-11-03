from django.shortcuts import render

# Create your views here.
from .forms import PacienteForm, RegistroEEGForm


def home(request):
    context = {

    }

    return render(request, "base.html", context)


def pacientes(request):

    form = PacienteForm(request.POST or None)
    context ={
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)

    return render(request, "pacientes.html", context)


def medicos(request):
    form = RegistroEEGForm

    context = {
        "form": form,
    }

    return render(request, "medicos.html", context)
