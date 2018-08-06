from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


def create_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_usuario')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro/usuario.html', { 'form' : form })


def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_cliente')
    else:
        form = ClienteForm()
    return render(request, 'cadastro/cliente.html', { 'form' : form })
