from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


def delete_usuario(request, id):
    delete_usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        delete_usuario.delete()
        return redirect('list_usuario')
    
    return render(request, "exclusaoConf.html", {'delete_usuario': delete_usuario})


def delete_cliente(request, id):
    delete_cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        delete_cliente.delete()
        return redirect('list_cliente')
    
    return render(request, "exclusaoConf.html", {'delete_cliente': delete_cliente})
