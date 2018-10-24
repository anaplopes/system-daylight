# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.fornecedorform import FornecedorForm 
from core.models.fornecedormodel import Fornecedor


@login_required(login_url='/entrar')
def create_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor cadastrado com sucesso.')
            return redirect('list_fornecedor')
        else:
            messages.error(request, form.errors)
            return render(request, 'comercial/cadastrarfornecedor.html', { 'form' : form })
    return render(request, 'comercial/cadastrarfornecedor.html', { 'form' : FornecedorForm() })


@login_required(login_url='/entrar')
def update_fornecedor(request, uuid):
    update_fornecedor = Fornecedor.objects.get(uuid=uuid)
    form = FornecedorForm(request.POST or None, instance=update_fornecedor)
    if form.is_valid():
        form.save()
        messages.success(request, 'Fornecedor atualizado com sucesso.')
        return redirect('list_fornecedor')
    else:
        messages.error(request, form.errors)
    return render(request, 'comercial/cadastrarfornecedor.html', { 'form' : form, 'update_fornecedor':update_fornecedor })


@login_required(login_url='/entrar')
def delete_fornecedor(request, uuid):
    delete_fornecedor = Fornecedor.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_fornecedor.delete()
        messages.success(request, 'Fornecedor excluído com sucesso.')
        return redirect('list_fornecedor')
    return render(request, "exclusaoConf.html", {'delete_fornecedor': delete_fornecedor})


@login_required(login_url='/entrar')
def list_fornecedor(request):
    template = "comercial/gerenciarfornecedor.html"
    if request.method == 'POST':
    
        nome_fornecedor = request.POST.get('nome_fornecedor')
        email_fornecedor = search = request.POST.get('email_fornecedor')
        numero_fiscal = request.POST.get('cpf/cnpj_fornecedor')

        if nome_fornecedor != "":
            lista_fornecedor = Fornecedor.objects.filter(fornecedorname__contains=nome_fornecedor)
        elif email_fornecedor != "":
            lista_fornecedor = Fornecedor.objects.filter(email__contains=email_fornecedor)
        elif numero_fiscal != "":
            lista_fornecedor = Fornecedor.objects.filter(numero_fiscal=numero_fiscal)
        else:
            return render(request, template)
        return render(request, template, {'lista_fornecedor': lista_fornecedor})
    else:
        return render(request, template)
