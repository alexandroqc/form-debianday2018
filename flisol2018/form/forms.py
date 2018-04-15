from django.forms import ModelForm

from form.models import Participante, TipoParticipacion

class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante
        fields = ['email', 'nombres', 'apellidos', 'telf', 'sexo', 'grupo', 'grado_academico', 'conoce_el_flisol', 'conoce_el_software_libre', 'ha_usado_software_libre', 'tipo_de_participacion', 'comentarios']
