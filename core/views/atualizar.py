# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.forms import *
from core.models import *

'''
@login_required(login_url='/entrar')
def update_usuario(request, user_id):
    getuser = User.objects.get(pk=user_id)
    update_usuario = CustomUser.objects.get(user_id=getuser)
    form = ProfileForm(request.POST or None, instance=update_usuario)
    if form.is_valid():
        form.save()
        return redirect('list_usuario')
    return render(request, 'gerencial/cadastrarprofile.html', { 'form' : form, 'update_usuario':update_usuario })
'''

@login_required(login_url='/entrar')
def update_cliente(request, uuid):
    update_cliente = Cliente.objects.get(uuid=uuid)
    form = ClienteForm(request.POST or None, instance=update_cliente)
    if form.is_valid():
        form.save()
        return redirect('list_cliente')
    return render(request, 'comercial/cadastrarcliente.html', { 'form' : form, 'update_cliente':update_cliente })


@login_required(login_url='/entrar')
def update_fornecedor(request, uuid):
    update_fornecedor = Fornecedor.objects.get(uuid=uuid)
    form = FornecedorForm(request.POST or None, instance=update_fornecedor)
    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')
    return render(request, 'comercial/cadastrarfornecedor.html', { 'form' : form, 'update_fornecedor':update_fornecedor })


@login_required(login_url='/entrar')
def update_prestador(request, uuid):
    update_prestador = PrestadorServico.objects.get(uuid=uuid)
    form = PrestadorForm(request.POST or None, instance=update_prestador)
    if form.is_valid():
        form.save()
        return redirect('list_prestador')
    return render(request, 'producao/cadastrarprestador.html', { 'form' : form, 'update_prestador':update_prestador })


@login_required(login_url='/entrar')
def update_material(request, uuid):
    update_material = Material.objects.get(uuid=uuid)
    form = MaterialForm(request.POST or None, instance=update_material)
    if form.is_valid():
        form.save()
        return redirect('list_material')
    return render(request, 'comercial/cadastrarmaterial.html', { 'form' : form, 'update_material':update_material })


@login_required(login_url='/entrar')
def update_medida(request, uuid):
    update_medida = UnidadeMedida.objects.get(uuid=uuid)
    form = UnidadeMedidaForm(request.POST or None, instance=update_medida)
    if form.is_valid():
        form.save()
        return redirect('create_medida')
    return render(request, 'comercial/cadastrarmedida.html', { 'form' : form, 'update_medida':update_medida })


@login_required(login_url='/entrar')
def update_produto(request, uuid):
    update_produto = Produto.objects.get(uuid=uuid)
    form = ProdutoForm(request.POST or None, instance=update_produto)
    if form.is_valid():
        form.save()
        return redirect('list_produto')
    return render(request, 'comercial/cadastrarproduto.html', { 'form' : form, 'update_produto':update_produto })


@login_required(login_url='/entrar')
def update_servico(request, uuid):
    update_servico = Servico.objects.get(uuid=uuid)
    form = ServicoForm(request.POST or None, instance=update_servico)
    if form.is_valid():
        form.save()
        return redirect('list_servico')
    return render(request, 'producao/cadastrarservico.html', { 'form' : form, 'update_servico':update_servico })
