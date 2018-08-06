from django.shortcuts import render
from core.forms import *
from core.models import *


def list_usuario(request):
    if request.method == 'POST':

        search = request.POST.get('nome_usuario')
        lista_usuario = Usuario.objects.filter(nome__contains=search)

        if search == "":
            search = request.POST.get('email_usuario')
            lista_usuario = Usuario.objects.filter(email__contains=search)

            if search == "":
                return render(request, "grupo/grupoUsuario.html")

        return render(request, "grupo/grupoUsuario.html", {'lista_usuario':lista_usuario})
    else:
        return render(request, "grupo/grupoUsuario.html")


def list_cliente(request):
    if request.method == 'POST':
        
        search = request.POST.get('nome_cliente')
        lista_cliente = Cliente.objects.filter(clientename__contains=search)

        if search == "":
            search = request.POST.get('email_cliente')
            lista_cliente = Cliente.objects.filter(email__contains=search)

            if search == "":
                search = request.POST.get('cpf/cnpj_cliente')
                lista_cliente = Cliente.objects.filter(numero_fiscal=search)

                if search == "":
                    return render(request, "grupo/grupoCliente.html")

        return render(request, "grupo/grupoCliente.html", {'lista_cliente':lista_cliente})
    else:
        return render(request, "grupo/grupoCliente.html")
