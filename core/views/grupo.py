from django.shortcuts import render
from core.forms import *
from core.models import *


def grupoUsuario(request):
    return render(request, "grupo/grupoUsuario.html")


def grupoCliente(request):
    return render(request, "grupo/grupoCliente.html")


def grupoFornecedor(request):
    return render(request, "grupo/grupoFornecedor.html")


def grupoPrestador(request):
    return render(request, "grupo/grupoPrestador.html")


def grupoProduto(request):
    return render(request, "grupo/grupoProduto.html")


def grupoServico(request):
    return render(request, "grupo/grupoServico.html")


def grupoMaterial(request):
    return render(request, "grupo/grupoMaterial.html")
