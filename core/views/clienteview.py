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
            messages.success(request, 'Cliente cadastrado com sucesso.', 'Sucesso')
            return redirect('list_cliente')
        else:
            tipo_erro = ''
            for erro in form.errors.values():
                tipo_erro += '\n'
                tipo_erro += erro[0]
            messages.error(request, tipo_erro, 'Erro')
            return render(request, 'comercial/cadastrarcliente.html', { 'form': form })
    return render(request, 'comercial/cadastrarcliente.html', { 'form': ClienteForm() })


@login_required(login_url='/entrar')
def update_cliente(request, uuid):
    update_cliente = Cliente.objects.get(uuid=uuid)
    form = ClienteForm(request.POST or None, instance=update_cliente)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente atualizado com sucesso.', 'Sucesso')
        return redirect('list_cliente')
    else:
        tipo_erro = ''
        for erro in form.errors.values():
            tipo_erro += '\n'
            tipo_erro += erro[0]
        messages.error(request, tipo_erro, 'Erro')
        return render(request, 'comercial/cadastrarcliente.html', { 'form' : form, 'update_cliente':update_cliente })


'''
@login_required(login_url='/entrar')
def delete_cliente(request, uuid):
    delete_cliente = Cliente.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso.', 'Sucesso')
        return redirect('list_cliente')
    return render(request, "exclusaoConf.html", {'delete_cliente': delete_cliente})
'''


@login_required(login_url='/entrar')
def list_cliente(request):
    template = "comercial/gerenciarcliente.html"
    if request.method == 'POST':

        nome_cliente = request.POST.get('nome_cliente')
        email_cliente = request.POST.get('email_cliente')
        numero_fiscal = request.POST.get('cpf/cnpj_cliente')

        if numero_fiscal != "":
            lista_cliente = Cliente.objects.filter(numero_fiscal=numero_fiscal)
            if lista_cliente.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif email_cliente != "":
            lista_cliente = Cliente.objects.filter(email=email_cliente)
            if lista_cliente.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif nome_cliente != "":
            lista_cliente = Cliente.objects.filter(clientename__contains=nome_cliente)
            if lista_cliente.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        else:
            messages.success(request, 'Nenhuma opção de pesquisa foi selecionada.', 'Erro')
            return render(request, template)
        return render(request, template, {'lista_cliente': lista_cliente})
    else:
        return render(request, template)
