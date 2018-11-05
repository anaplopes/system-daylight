# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.models.tecidomodel import Tecido
from core.forms.tecidoform import TecidoForm


@login_required(login_url='/entrar')
def create_tecido(request):
    template = 'comercial/cadastrartecido.html'
    if request.method == 'POST':
        form = TecidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tecido cadastrado com sucesso.', 'Sucesso')
            return redirect('list_tecido')
        else:
            tipo_erro = ''
            for erro in form.errors.values():
                tipo_erro += '\n'
                tipo_erro += erro[0]
            messages.error(request, tipo_erro, 'Erro')
            return render(request, template, { 'form' : form })
    return render(request, template, { 'form' : TecidoForm() })


@login_required(login_url='/entrar')
def update_tecido(request, uuid):
    template = 'comercial/cadastrartecido.html'
    update_tecido = Tecido.objects.get(uuid=uuid)
    form = TecidoForm(request.POST or None, instance=update_tecido)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tecido atualizado com sucesso.', 'Sucesso')
        return redirect('list_tecido')
    else:
        tipo_erro = ''
        for erro in form.errors.values():
            tipo_erro += '\n'
            tipo_erro += erro[0]
        messages.error(request, tipo_erro, 'Erro')
    return render(request, template, { 'form' : form, 'update_tecido':update_tecido })


@login_required(login_url='/entrar')
def delete_tecido(request, uuid):
    delete_tecido = Tecido.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_tecido.delete()
        messages.success(request, 'Tecido excluído com sucesso.', 'Sucesso')
        return redirect('list_tecido')
    return render(request, "exclusaoConf.html", { 'delete_tecido': delete_tecido })


@login_required(login_url='/entrar')
def list_tecido(request):
    template = "comercial/gerenciartecido.html"
    if request.method == 'POST':

        tipo_tecido = request.POST.get('tipo_tecido')
        fabricante = request.POST.get('fabricante')
        desc_tecido = request.POST.get('desc_tecido')

        if tipo_tecido != "":
            lista_tecido = Tecido.objects.filter(tipo_tecido__contains=tipo_tecido)
        elif fabricante != "":
            lista_tecido = Tecido.objects.filter(nome_fabricante__contains=fabricante)
        elif desc_tecido != "":
            lista_tecido = Tecido.objects.filter(tecido__contains=desc_tecido)
        else:
            return render(request, template)
        return render(request, template, { 'lista_tecido': lista_tecido })
    else:
        return render(request, template)
