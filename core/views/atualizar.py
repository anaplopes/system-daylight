from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


def update_usuario(request, id):
    update_usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST or None, instance=update_usuario)

    if form.is_valid():
        form.save()
        return redirect('list_usuario')

    return render(request, 'cadastro/usuario.html', { 'form' : form, 'update_usuario':update_usuario })


def update_cliente(request, id):
    update_cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=update_cliente)

    if form.is_valid():
        form.save()
        return redirect('list_cliente')

    return render(request, 'cadastro/cliente.html', { 'form' : form, 'update_cliente':update_cliente })