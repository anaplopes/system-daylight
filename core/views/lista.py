from django.shortcuts import render
from core.forms import *
from core.models import *


def list_usuario(request):
    lista_usuario = Usuario.objects.filter(nome__contains='ana')
    return render(request, "grupo/grupoUsuario.html", { 'lista_usuario' : lista_usuario })
