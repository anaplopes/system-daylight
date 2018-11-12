# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.prestadorform import PrestadorForm
from core.models.prestadormodel import PrestadorServico


@login_required(login_url='/entrar')
def create_prestador(request):
    if request.method == 'POST':
        form = PrestadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prestador cadastrado com sucesso.', 'Sucesso')
            return redirect('list_prestador')
        else:
            tipo_erro = ''
            for erro in form.errors.values():
                tipo_erro += '\n'
                tipo_erro += erro[0]
            messages.error(request, tipo_erro, 'Erro')
            return render(request, 'producao/cadastrarprestador.html', { 'form' : form })
    return render(request, 'producao/cadastrarprestador.html', { 'form' : PrestadorForm() })


@login_required(login_url='/entrar')
def update_prestador(request, uuid):
    update_prestador = PrestadorServico.objects.get(uuid=uuid)
    form = PrestadorForm(request.POST or None, instance=update_prestador)
    if form.is_valid():
        form.save()
        messages.success(request, 'Prestador atualizado com sucesso.', 'Sucesso')
        return redirect('list_prestador')
    else:
        tipo_erro = ''
        for erro in form.errors.values():
            tipo_erro += '\n'
            tipo_erro += erro[0]
        messages.error(request, tipo_erro, 'Erro')
    return render(request, 'producao/cadastrarprestador.html', { 'form' : form, 'update_prestador':update_prestador })


@login_required(login_url='/entrar')
def delete_prestador(request, uuid):
    delete_prestador = PrestadorServico.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_prestador.delete()
        messages.success(request, 'Prestador excluído com sucesso.', 'Sucesso')
        return redirect('list_prestador')
    return render(request, "exclusaoConf.html", {'delete_prestador': delete_prestador})


@login_required(login_url='/entrar')
def list_prestador(request):
    template = "producao/gerenciarprestador.html"
    if request.method == 'POST':

        nome_prestador = request.POST.get('nome_prestador')
        email_prestador = request.POST.get('email_prestador')
        numero_fiscal = request.POST.get('cpf/cnpj_prestador')

        if numero_fiscal != "":
            lista_prestador = PrestadorServico.objects.filter(numero_fiscal=numero_fiscal)
            if lista_prestador.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif email_prestador != "":
            lista_prestador = PrestadorServico.objects.filter(email=email_prestador)
            if lista_prestador.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif nome_prestador != "":
            lista_prestador = PrestadorServico.objects.filter(prestadorname__contains=nome_prestador)
            if lista_prestador.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        else:
            messages.success(request, 'Nenhuma opção de pesquisa foi selecionada.', 'Erro')
            return render(request, template)
        return render(request, template, {'lista_prestador': lista_prestador})
    else:
        return render(request, template)
