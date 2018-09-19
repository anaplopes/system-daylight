# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


@login_required(login_url='/entrar')
def create_usuario(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('list_usuario')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'gerencial/cadastrarusuario.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required(login_url='/entrar')
def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso.')
        return redirect('list_cliente')
    else:
        form = ClienteForm()
        messages.error(request, form.errors)
    return render(request, 'comercial/cadastrarcliente.html', { 'form' : form })


@login_required(login_url='/entrar')
def create_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor cadastrado com sucesso.')
        return redirect('list_fornecedor')
    else:
        form = FornecedorForm()
        messages.error(request, form.errors)
    return render(request, 'comercial/cadastrarfornecedor.html', { 'form' : form })


@login_required(login_url='/entrar')
def create_prestador(request):
    if request.method == 'POST':
        form = PrestadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prestador cadastrado com sucesso.')
        return redirect('list_prestador')
    else:
        form = PrestadorForm()
        messages.error(request, form.errors)
    return render(request, 'producao/cadastrarprestador.html', { 'form' : form })


@login_required(login_url='/entrar')
def create_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        tipo_mprima = request.POST.get('tipo_mprima')
        if form.is_valid():
            form.save()
            messages.success(request, 'Material cadastrado com sucesso.')
            if tipo_mprima == 'Tecido' or tipo_mprima == 'tecido':
                return redirect('create_medida')
            else:
                return redirect('list_material')
    else:
        form = MaterialForm()
        messages.error(request, form.errors)
    return render(request, 'comercial/cadastrarmaterial.html', { 'form' : form})


@login_required(login_url='/entrar')
def create_medida(request):
    if request.method == 'POST':
        form = UnidadeMedidaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medida cadastrado com sucesso.')
            return redirect('list_medida')
    else:
        form = UnidadeMedidaForm()
        messages.error(request, form.errors)
    return render(request, 'comercial/cadastrarmedida.html', { 'form' : form })


@login_required(login_url='/entrar')
def create_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso.')
        return redirect('list_produto')
    else:
        form = ProdutoForm()
        messages.error(request, form.errors)
    return render(request, 'comercial/cadastrarproduto.html', { 'form' : form })


@login_required(login_url='/entrar')
def create_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço cadastrado com sucesso.')
        return redirect('list_servico')
    else:
        form = ServicoForm()
        messages.error(request, form.errors)
    return render(request, 'producao/cadastrarservico.html', { 'form' : form })
