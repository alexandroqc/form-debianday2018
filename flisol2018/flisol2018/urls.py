"""flisol2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#from form.views import ParticipanteCreateView, ParticipanteList
from form.views import participanteCreate, participanteDetalle, lista
urlpatterns = [
    path('admin/', admin.site.urls),
    # formulario de participacion
    path('', participanteCreate, name='registrar-participante'),
    #path('p/<int:pk>', participanteDetalle, name='participante-detalle'),
    path('par/<slug:slg>/', participanteDetalle, name='participante-detalle'),
    path('par/<slug:slg>/<slug:md>', participanteDetalle, name='participante-detalle'),
    path('p/lista/', lista, name='lista'),
    path('p/lista/<slug:slg>', lista, name='lista_mas'),
]
