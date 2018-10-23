# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.clienteform import ClienteForm
from core.models.clientemodel import Cliente


@login_required(login_url='/entrar')
def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso.')
            return redirect('list_cliente')
        else:
            messages.error(request, form.errors)
            return render(request, 'comercial/cadastrarcliente.html', { 'form' : form })
    return render(request, 'comercial/cadastrarcliente.html', { 'form' : ClienteForm() })


@login_required(login_url='/entrar')
def update_cliente(request, uuid):
    update_cliente = Cliente.objects.get(uuid=uuid)
    form = ClienteForm(request.POST or None, instance=update_cliente)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente atualizado com sucesso.')
        return redirect('list_cliente')
    else:
        messages.error(request, form.errors)
        return render(request, 'comercial/cadastrarcliente.html', { 'form' : form, 'update_cliente':update_cliente })


@login_required(login_url='/entrar')
def delete_cliente(request, uuid):
    delete_cliente = Cliente.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso.')
        return redirect('list_cliente')
    return render(request, "exclusaoConf.html", {'delete_cliente': delete_cliente})


@login_required(login_url='/entrar')
def list_cliente(request):
    template = "comercial/gerenciarcliente.html"
    if request.method == 'POST':
        
        nome_cliente = request.POST.get('nome_cliente')
        email_cliente = request.POST.get('email_cliente')
        numero_fiscal = request.POST.get('cpf/cnpj_cliente')

        if nome_cliente is not None:
            lista_cliente = Cliente.objects.filter(clientename__contains=nome_cliente)
        elif email_cliente is not None:
            lista_cliente = Cliente.objects.filter(email__contains=email_cliente)
        elif numero_fiscal is not None:
            lista_cliente = Cliente.objects.filter(numero_fiscal=numero_fiscal)
        else:
            return render(request, template)
        return render(request, template, {'lista_cliente':lista_cliente})
    else:
        return render(request, template)
