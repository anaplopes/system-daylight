# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


@login_required(login_url='/entrar')
def delete_usuario(request, uuid):
    delete_usuario = Profile.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_usuario.delete()
        return redirect('list_usuario')
    return render(request, "exclusaoConf.html", {'delete_usuario': delete_usuario})


@login_required(login_url='/entrar')
def delete_cliente(request, uuid):
    delete_cliente = Cliente.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_cliente.delete()
        return redirect('list_cliente')
    return render(request, "exclusaoConf.html", {'delete_cliente': delete_cliente})


@login_required(login_url='/entrar')
def delete_fornecedor(request, uuid):
    delete_fornecedor = Fornecedor.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_fornecedor.delete()
        return redirect('list_fornecedor')
    return render(request, "exclusaoConf.html", {'delete_fornecedor': delete_fornecedor})


@login_required(login_url='/entrar')
def delete_prestador(request, uuid):
    delete_prestador = PrestadorServico.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_prestador.delete()
        return redirect('list_prestador')
    return render(request, "exclusaoConf.html", {'delete_prestador': delete_prestador})


@login_required(login_url='/entrar')
def delete_material(request, uuid):
    delete_material = Material.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_material.delete()
        return redirect('list_material')
    return render(request, "exclusaoConf.html", {'delete_material': delete_material})


@login_required(login_url='/entrar')
def delete_medida(request, uuid):
    delete_medida = UnidadeMedida.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_medida.delete()
        return redirect('create_medida')
    return render(request, "exclusaoConf.html", {'delete_medida': delete_medida})


@login_required(login_url='/entrar')
def delete_produto(request, uuid):
    delete_produto = Produto.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_produto.delete()
        return redirect('list_produto')
    return render(request, "exclusaoConf.html", {'delete_produto': delete_produto})


@login_required(login_url='/entrar')
def delete_servico(request, uuid):
    delete_servico = Servico.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_servico.delete()
        return redirect('list_servico')
    return render(request, "exclusaoConf.html", {'delete_servico': delete_servico})
