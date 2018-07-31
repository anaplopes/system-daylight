from django.shortcuts import render
from core.forms import *
from core.models import *


def list_usuario(request):
    if request.method == 'POST':
        search = request.POST.get('nome')
        lista_usuario = Usuario.objects.filter(nome__contains=search)
        return render(request, "grupo/grupoUsuario.html", {'lista_usuario':lista_usuario})
    else:
        return render(request, "grupo/grupoUsuario.html")