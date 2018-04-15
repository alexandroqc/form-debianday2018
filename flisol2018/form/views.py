from django.shortcuts import render

from django.template.response import TemplateResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect

from django.http import Http404
from django.shortcuts import render
#from django.core.urlresolvers import reverse

from .models import Participante, TipoParticipacion
from .forms import ParticipanteForm

# Create your views here.
class ParticipanteList(ListView):
    model = Participante

class ParticipanteCreateView(CreateView):
    model = Participante
    fields = ['email', 'nombres', 'apellidos', 'telf', 'sexo', 'grupo', 'grado_academico', 'conoce_el_flisol', 'conoce_el_software_libre', 'ha_usado_software_libre', 'tipo_de_participacion', 'comentarios']

    def form_valid(self, form):
        #form.instance.created_by = self.request.user
        print(super().form_valid(form))
        #return super().form_valid(form)
        return HttpResponse("vamos")


def participanteCreate(request):
    if request.method == "GET":
        form = ParticipanteForm()
        return render(request, 'form/participante_form.html', {'form':form})

    if request.method == "POST":
        form = ParticipanteForm(request.POST)
        print(form.is_valid())
        print('errors:   >>>'+str(form.errors))
        if not form.is_valid():
            return HttpResponse("Error al llenar el formulario")

        participante = form.save()
        print ("PAR",str(participante))

        # creando el tipo de participacion
        tipo = TipoParticipacion()
        tipo.participante = participante
        if request.POST.get('tipo_participacion_val') == 'asistente':
            tipo.tipo = 'asistente'
            tipo.asistente = True
            tipo.asistente_software_deseado = request.POST.get('asistente_software_deseado')
        if request.POST.get('tipo_participacion_val') == 'expositor':
            tipo.tipo = 'expositor'
            tipo.expositor = True
            tipo.expositor_software_manejado = request.POST.get('expositor_software_manejado')
            tipo.expositor_tema = request.POST.get('expositor_tema')
        if request.POST.get('tipo_participacion_val') == 'logistica':
            tipo.tipo = 'logistica'
            tipo.logistica = True
            tipo.logistica_tipo = request.POST.get('logistica_tipo')
        if request.POST.get('tipo_participacion_val') == 'instalador':
            tipo.tipo = 'instalador'
            tipo.instalador = True
            tipo.instalador_capacitacion = request.POST.get('instalador_capacitacion')
            tipo.instalador_tipo_software = request.POST.get('instalador_tipo_software')
        if request.POST.get('tipo_participacion_val') == 'otro':
            tipo.tipo = 'otro'
            tipo.otro = True
            tipo.otro_desc = request.POST.get('ayuda_otro')
        tipo.save()

        return HttpResponseRedirect('/p/'+str(participante.id))
    #return HttpResponse("hecho?")

def participanteDetalle(request, pk):
    try:
        p = Participante.objects.get(pk=pk)
        t = TipoParticipacion.objects.get(participante=p)
    except Participante.DoesNotExist:
        raise Http404("No existe ese participante")
    return render(request, 'form/participante_detalle.html',
                  {'participante':p,
                   'tipo': t
                  })

def lista(request):
    if request.method == "GET":
        p = []
        participantes = Participante.objects.all()
        for par in participantes:
            try:
                tipo = TipoParticipacion.objects.get(participante=par)
                print(tipo)
                obj = {'p':par, 'tipo': tipo}
                p.append(obj)
            except TipoParticipacion.DoesNotExist:
                print("error", str(par))
        return render(request, 'form/participante_lista.html',
                          {'participantes': p})
