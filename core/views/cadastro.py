from django.shortcuts import render
from core.forms import *
from core.models import *


def usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(request, 'cadastro/usuario.html', { "form" : form })


def cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'cadastro/cliente.html', { "form" : form })


def fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FornecedorForm()
    return render(request, 'cadastro/fornecedor.html', { "form" : form })


def prestador(request):
    if request.method == 'POST':
        form = PrestadorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PrestadorForm()
    return render(request, 'cadastro/prestador.html', { "form" : form })


def produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProdutoForm()
    return render(request, 'cadastro/produto.html', { "form" : form })


def servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ServicoForm()
    return render(request, 'cadastro/servico.html', { "form" : form })


def material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MaterialForm()
    return render(request, 'cadastro/material.html', { "form" : form })


def unidadeMedida(request):
    if request.method == 'POST':
        form = UnidadeMedidaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UnidadeMedidaForm()
    return render(request, 'cadastro/unidadeMedida.html', { "form" : form })
