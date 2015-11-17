from django.shortcuts import render, render_to_response
from django.template import RequestContext
from matplotlib import pylab
from PIL import Image
# Create your views here.
from .forms import PacienteForm, RegistroEEGForm
from .models import RegistroEEG, Paciente



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
    form = RegistroEEGForm(request.POST or None)

    if form.is_valid():
        print form.cleaned_data
    context = {
        "form": form,
    }

    return render(request, "medicos.html", context)


def registros(request):
    # Handle file upload
    if request.method == 'POST':
        form = RegistroEEGForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            render(request, "registros.html", {})
    else:
        form = RegistroEEGForm() # A empty, unbound form

    # Load documents for the list page
    registros_eeg = RegistroEEG.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'registros.html',
        {'registros': registros_eeg, 'form': form},
        context_instance=RequestContext(request)
    )


def registroDinamico(request):
    # Generate 'png' image form .mat data
    pass

