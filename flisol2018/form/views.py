from django.shortcuts import render
import hashlib

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

from flisol2018.settings import SECRET_1

# Create your views here.
def participanteCreate(request):
    if request.method == "GET":
        form = ParticipanteForm()
        return render(request, 'form/participante_form.html', {'form':form})

    if request.method == "POST":
        print (request.POST)
        form = ParticipanteForm(request.POST)
        print(form.is_valid())
        #print('errors:   >>>'+str(form.errors))
        if not form.is_valid():
            return HttpResponse("Error al llenar el formulario")

        participante = form.save()
        print ("PAR",str(participante))

        # creando el tipo de participacion                          
        tipo = TipoParticipacion()
        try:
            tipo.participante = participante
        except Exception as error:
            print ("error al crear tipo", error)
            
        if request.POST.get('tipo_participacion_val') == 'asistente':
            tipo.tipo = 'asistente'
            tipo.asistente = True
            tipo.asistente_software_deseado = request.POST.get('asistente_software_deseado')
        elif request.POST.get('tipo_participacion_val') == 'expositor':
            tipo.tipo = 'expositor'
            tipo.expositor = True
            tipo.expositor_software_manejado = request.POST.get('expositor_software_manejado')
            tipo.expositor_tema = request.POST.get('expositor_tema')
        elif request.POST.get('tipo_participacion_val') == 'logistica':
            tipo.tipo = 'logistica'
            tipo.logistica = True
            tipo.logistica_tipo = request.POST.get('logistica_tipo')
        elif request.POST.get('tipo_participacion_val') == 'instalador':
            tipo.tipo = 'instalador'
            tipo.instalador = True
            if (request.POST.get('instalador_capacitacion') == 'on'):
                tipo.instalador_capacitacion = True
            else:
                tipo.instalador_capacitacion = False
            tipo.instalador_tipo_software = request.POST.get('instalador_tipo_software')
        elif request.POST.get('tipo_participacion_val') == 'mesa':
            tipo.tipo = 'mesa'
        elif request.POST.get('tipo_participacion_val') == 'otro':
            tipo.tipo = 'otro'
            tipo.otro = True
            tipo.otro_desc = request.POST.get('ayuda_otro')
        tipo.save()
        
        ruta = hashlib.sha1(SECRET_1.encode('utf-8')*(participante.id)).hexdigest()
        print (ruta)
        return HttpResponseRedirect('/par/'+ruta)
    #return HttpResponse("hecho?")

def participanteDetalle(request, slg, md=' '):
    # buscando el slug que tenga que ver con la clave
    p_id = -1
    for p in Participante.objects.all():
        test = hashlib.sha1(SECRET_1.encode('utf-8')*p.id).hexdigest()
        if test == slg:
            p_id = p.id
            break;
        
    if p_id <= 0:
        print('no funciona ese', slg)
        raise Http404("No existe ese participante")
    
    try:
        p = Participante.objects.get(pk=p_id)
        t = TipoParticipacion.objects.get(participante=p)
    except Participante.DoesNotExist as e:
        print ('error:', e)
        raise Http404("No existe ese participante")

    return render(request, 'form/participante_detalle.html',
                  {'participante':p,
                   'tipo': t,
                   'mas_detalles': md.count('_')>0
                  })

def lista(request, slg=''):
    if request.method == "GET":
        p = []

        numAsistentes = numExpositores = numLogistica = numMesas = 0
        total = numOtro = 0
        try:
            numAsistentes = TipoParticipacion.objects.filter(tipo='asistente').count()
            numExpositores = TipoParticipacion.objects.filter(tipo='expositor').count()
            numLogistica = TipoParticipacion.objects.filter(tipo='logistica').count()
            numMesas = TipoParticipacion.objects.filter(tipo='mesa').count()
            numOtro = TipoParticipacion.objects.filter(tipo='otro').count()
            total = TipoParticipacion.objects.all().count()
        except Exception as e:
            print ("error:", e)

        participantes = Participante.objects.all()
        for par in participantes:
            try:
                tipo = TipoParticipacion.objects.get(participante=par)
                slug = hashlib.sha1(SECRET_1.encode('utf-8')*par.id).hexdigest()
                obj = {'p':par, 'tipo': tipo, 'slug': slug}
                p.append(obj)
            except TipoParticipacion.DoesNotExist as e:
                print("error", str(par), str(e))
        return render(request, 'form/participante_lista.html',
                          {'participantes': p ,
                           'mas_detalles': slg.count('_')>0,
                           'expositores': numExpositores,
                           'asistentes': numAsistentes,
                           'logistica': numLogistica,
                           'mesas': numMesas,
                           'otro': numOtro,
                           'total': total})

