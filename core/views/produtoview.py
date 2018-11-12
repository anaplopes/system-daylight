# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.produtoform import ProdutoForm
from core.models.produtomodel import Produto


@login_required(login_url='/entrar')
def create_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso.', 'Sucesso')
            return redirect('list_produto')
        else:
            tipo_erro = ''
            for erro in form.errors.values():
                tipo_erro += '\n'
                tipo_erro += erro[0]
            messages.error(request, tipo_erro, 'Erro')
            return render(request, 'comercial/cadastrarproduto.html', { 'form' : form })
    return render(request, 'comercial/cadastrarproduto.html', { 'form' : ProdutoForm() })


@login_required(login_url='/entrar')
def update_produto(request, uuid):
    update_produto = Produto.objects.get(uuid=uuid)
    form = ProdutoForm(request.POST or None, instance=update_produto)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produto atualizado com sucesso.', 'Sucesso')
        return redirect('list_produto')
    else:
        tipo_erro = ''
        for erro in form.errors.values():
            tipo_erro += '\n'
            tipo_erro += erro[0]
        messages.error(request, tipo_erro, 'Erro')
    return render(request, 'comercial/cadastrarproduto.html', { 'form' : form, 'update_produto':update_produto })


@login_required(login_url='/entrar')
def delete_produto(request, uuid):
    delete_produto = Produto.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_produto.delete()
        messages.success(request, 'Produto excluído com sucesso.', 'Sucesso')
        return redirect('list_produto')
    return render(request, "exclusaoConf.html", {'delete_produto': delete_produto})


@login_required(login_url='/entrar')
def list_produto(request):
    template = "comercial/gerenciarproduto.html"
    if request.method == 'POST':

        tipo_produto = request.POST.get('tipo_produto')
        class_produto = request.POST.get('classificacao_produto')
        desc_produto = request.POST.get('desc_produto')

        if tipo_produto != "":
            lista_produto = Produto.objects.filter(tipo_produto__contains=tipo_produto)
            if lista_produto.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif class_produto != "":
            lista_produto = Produto.objects.filter(classificacao__contains=class_produto)
            if lista_produto.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif desc_produto != "":
            lista_produto = Produto.objects.filter(produto__contains=desc_produto)
            if lista_produto.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        else:
            messages.success(request, 'Nenhuma opção de pesquisa foi selecionada.', 'Erro')
            return render(request, template)
        return render(request, template, {'lista_produto': lista_produto})
    else:
        return render(request, template)
