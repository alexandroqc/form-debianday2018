from django.db import models

# Create your models here.

SEXO_CHOICES = [
    ('Mujer', 'Mujer'),
    ('Hombre', 'Hombre'),
    ('Prefiero no decirlo', 'prefiero no decirlo')
]

GRADO_ACADEMICO_CHOICES = [
    ('Bachiller', 'Bachiller'),
    ('Técnico', 'Técnico'),
    ('Licenciatura', 'Licenciatura'),
    ('Magíster', 'Maǵister'),
    ('Doctor', 'Doctor'),
    ('Prefiero no indicar', '-'),
]

PARTICIPACION_CHOICES = [
    ('Quiero que me ayuden a instalar software libre en mi computadora','Sólo asistir'),
    ('Como expositor con el tema:','Exponer un tema'),
    ('Ayudando en la instalación de software el día del FLISOL o capacitando a otros para ser instaladores', 'Instalador'),
    ('Me gustaría una mesa para hablar de una tematica relacionada al software libre','Mesa de debate'),
    ('Quiero ayudar en la organización y logística del evento','Logística'),
    ('Otro', 'otro')
]

class Participante(models.Model):
    email = models.EmailField(max_length=254,
                              help_text='Registre su correo electrónico')

    nombres = models.CharField(max_length=500)
    apellidos = models.CharField(max_length=500)

    telf = models.CharField(max_length=100,
                            default=" ",
                            help_text="Número de teléfono móvil (opcional)")
    
    sexo = models.CharField(max_length=20,
                            default=' ',
                            choices=SEXO_CHOICES)
    grupo = models.CharField(max_length=300,
                             default=' ',
                             help_text="Grupo o asociación a la que pertenece (Pude dejar en blanco)")
    grado_academico = models.CharField(max_length=300,
                                       choices=GRADO_ACADEMICO_CHOICES,
                                       default="prefiero no especificar",
                                       help_text="Máximo grado académico alcanzado")

    conoce_el_flisol = models.BooleanField(default=False,
                                        help_text="¿Sabe que es el FLISOL?")
    conoce_el_software_libre = models.BooleanField(default=False,
                                                help_text="¿Conoce el Software Libre?")

    ha_usado_software_libre = models.BooleanField(default=False, help_text="¿Ha usado software libre?")

    tipo_de_participacion = models.CharField(max_length=1000,
                                          default=PARTICIPACION_CHOICES[0],
                                          choices=PARTICIPACION_CHOICES,
                                          help_text="Seleccione la forma en la que desea participar")
    comentarios = models.CharField(max_length=1000,
                                   default=" ",
                                   help_text='Comentarios o sugerencias para la organización del evento')

    def __str__(self):
        r = str(self.id)+":<"+self.email+'> '+self.nombres+' '+self.apellidos + ', tipo:' + str(self.tipo_participacion)
        return r

    def get_absolute_url(self):
        return reverse('participante-detalle', kwargs={'pk': self.pk})
    
INSTALADOR_TIPO_SOFTWARE_CHOICES = [
    ("Sistemas Operativos libres para PC","Sistemas Operativos libres para PC"),
    ("Sistemas Operativos libres para Moviles","Sistemas Operativos libres para Moviles"),
    ("Programas libres para diferentes temáticas (favor describir que temáticas o programas en la opción 'Otros')", "Programas libres para diferentes temáticas"),
    ("Otro","Otro")
]

LOGISTICA_TIPO_CHOICES = [
    ("Apoyo logístico en la organización y gestión del evento.","Apoyo logístico en la organización y gestión del evento."),
    ("Difusión en redes sociales","Difusión en redes sociales"),
    ("Difusión en prensa y otros medios de comunicación","Difusión en prensa y otros medios de comunicación"),
    ("Difusión en prensa y otros medios de comunicación","Difusión en prensa y otros medios de comunicación"),
    ("Otro", "Otro")
]

ASISTENTE_SOFTWARE_DESEADO_CHOICES = [
    ("Educativo","Educativo"),
    ("Para Internet","Para Internet"),
    ("Juegos","Juegos"),
    ("Multimadia","Multimedia"),
    ("Accesorios","Accesorios"),
    ("Diseño gráfico","Diseño gráfico"),
    ("Seguridad","Seguridad"),
    ("Oficina", "Oficina"),
    ("Programación","Programación"),
    ("Científico","Científico"),
    ("Otro","Otro")
]
    
class TipoParticipacion(models.Model):
    participante = models.ForeignKey('Participante',
                                     default=1,
                                     on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1000,
                            default=PARTICIPACION_CHOICES[0])

    # expositores
    expositor = models.BooleanField(default=False)
    expositor_software_manejado = models.CharField(max_length=1000,
                                                     help_text="Por favor indica algunos ejemplos del software libre que has manejado (y si gustas algunos ejemplos del uso que le has dado)",
                                                   default=" ")
    expositor_tema = models.CharField(max_length=500,
                                      help_text="Indica el tema que desea exponer",
                                      default=" ")

    # asistentes
    asistente = models.BooleanField(default=False)
    asistente_software_deseado = models.CharField(max_length=500,
                                                  choices=ASISTENTE_SOFTWARE_DESEADO_CHOICES,
                                                  default=ASISTENTE_SOFTWARE_DESEADO_CHOICES[0])
    asistente_otro_desc = models.CharField(max_length=500,
                                           default=" ")
    
    # para instaladores
    instalador = models.BooleanField(default=False)
    instalador_capacitacion = models.BooleanField(default=True,
                                                  help_text="Requeriré capacitación para para ayudar como instalador")
    instalador_tipo_software = models.CharField(max_length=500,
                                                default=INSTALADOR_TIPO_SOFTWARE_CHOICES[0],
                                                choices=INSTALADOR_TIPO_SOFTWARE_CHOICES,
                                                help_text="Indica el tipo de software que nos podrías ayudar a instalar")

    # para colaboradores en logistica
    logistica = models.BooleanField(default=False)
    logistica_tipo = models.CharField(max_length=500,
                                      choices=LOGISTICA_TIPO_CHOICES)
    logistica_otro_desc = models.CharField(max_length=1000,
                                           default=" ")

    # otro tipo de ayuda
    otro = models.BooleanField(default=False)
    otro_desc = models.CharField(max_length=1000,
                                 default=" ")
    
    def __str__(self):
        r = str(self.id) + ') instaldor:' + str(self.instaldor) + ' ,asistente:' + str(self.asistente) + ' ,expositor: ' + str(self.expositor)+ " ,logistica: " +str(self.logistica) + " ,otro" + str(self.otro)
        return r

