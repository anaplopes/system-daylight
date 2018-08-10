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


def create_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_fornecedor')
    else:
        form = FornecedorForm()
    return render(request, 'cadastro/fornecedor.html', { 'form' : form })


def create_prestador(request):
    if request.method == 'POST':
        form = PrestadorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_prestador')
    else:
        form = PrestadorForm()
    return render(request, 'cadastro/prestador.html', { 'form' : form })


def create_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_material')
    else:
        form = MaterialForm()
    return render(request, 'cadastro/material.html', { 'form' : form })


def create_medida(request):
    if request.method == 'POST':
        form = UnidadeMedidaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_medida')
    else:
        form = UnidadeMedidaForm()
    return render(request, 'cadastro/unidadeMedida.html', { 'form' : form })


def create_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_produto')
    else:
        form = ProdutoForm()
    return render(request, 'cadastro/produto.html', { 'form' : form })


def create_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_servico')
    else:
        form = ServicoForm()
    return render(request, 'cadastro/servico.html', { 'form' : form })
