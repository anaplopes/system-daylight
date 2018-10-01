# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.medidaform import UnidadeMedidaForm
from core.models.medidamodel import UnidadeMedida


@login_required(login_url='/entrar')
def create_medida(request):
    if request.method == 'POST':
        form = UnidadeMedidaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medida cadastrado com sucesso.')
            return redirect('list_medida')
        else:
            messages.error(request, form.errors)
            return render(request, 'comercial/cadastrarmedida.html', { 'form' : form })
    return render(request, 'comercial/cadastrarmedida.html', { 'form' : UnidadeMedidaForm() })


@login_required(login_url='/entrar')
def update_medida(request, uuid):
    update_medida = UnidadeMedida.objects.get(uuid=uuid)
    form = UnidadeMedidaForm(request.POST or None, instance=update_medida)
    if form.is_valid():
        form.save()
        messages.success(request, 'Medida atualizada com sucesso.')
        return redirect('create_medida')
    else:
        messages.error(request, form.errors)
    return render(request, 'comercial/cadastrarmedida.html', { 'form' : form, 'update_medida':update_medida })


@login_required(login_url='/entrar')
def delete_medida(request, uuid):
    delete_medida = UnidadeMedida.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_medida.delete()
        messages.success(request, 'Medida excluído com sucesso.')
        return redirect('create_medida')
    return render(request, "exclusaoConf.html", {'delete_medida': delete_medida})


@login_required(login_url='/entrar')
def list_medida(request):
    template = "comercial/cadastrarmedida.html"
    search = request.POST.get('tecido')
    lista_medida = UnidadeMedida.objects.filter(tecido_id=search)
    return render(requeste, template, {'lista_medida':lista_medida})
