# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.servicoform import ServicoForm
from core.models.servicomodel import Servico


@login_required(login_url='/entrar')
def create_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço cadastrado com sucesso.')
            return redirect('list_servico')
        else:
            messages.error(request, form.errors)
            return render(request, 'producao/cadastrarservico.html', { 'form' : form })
    return render(request, 'producao/cadastrarservico.html', { 'form' : ServicoForm() })


@login_required(login_url='/entrar')
def update_servico(request, uuid):
    update_servico = Servico.objects.get(uuid=uuid)
    form = ServicoForm(request.POST or None, instance=update_servico)
    if form.is_valid():
        form.save()
        return redirect('list_servico')
    else:
        messages.error(request, form.errors)
    return render(request, 'producao/cadastrarservico.html', { 'form' : form, 'update_servico':update_servico })


@login_required(login_url='/entrar')
def delete_servico(request, uuid):
    delete_servico = Servico.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_servico.delete()
        return redirect('list_servico')
    return render(request, "exclusaoConf.html", {'delete_servico': delete_servico})


@login_required(login_url='/entrar')
def list_servico(request):
    template = "producao/gerenciarservico.html"
    if request.method == 'POST':
        search = request.POST.get('tipo_servico')
        lista_servico = Servico.objects.filter(tipo_servico=search)
        if search == "--Selecione--":
            search = request.POST.get('servico')
            lista_servico = Servico.objects.filter(servico=search)
            if search == "--Selecione--":
                return render(request, template)
        return render(request, template, {'lista_servico':lista_servico})
    else:
        return render(request, template)
