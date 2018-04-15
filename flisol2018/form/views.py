from django.shortcuts import render

from django.template.response import TemplateResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from .models import Participante, TipoParticipacion

# Create your views here.
class ParticipanteList(ListView):
    model = Participante

class ParticipanteCreateView(CreateView):
    model = Participante
    fields = ['email', 'nombres', 'apellidos', 'telf', 'sexo', 'grupo', 'grado_academico', 'conoce_el_flisol', 'conoce_el_software_libre', 'ha_usado_software_libre', 'tipo_de_participacion', 'comentarios']
