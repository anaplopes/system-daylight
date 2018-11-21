# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from core.views.login import check_gerente
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.compraform import CompraForm
from core.models.compramodel import Compra
from core.models.fornecedormodel import Fornecedor
from core.models.itemcompramodel import ItemCompra
from core.forms.itemcompraform import ItemCompraForm
from django.forms import inlineformset_factory


@user_passes_test(check_gerente, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def register_compra(request):
    template = 'comercial/registrarcompra.html'

    instance_compra = Compra()
    form_compra = CompraForm(instance=instance_compra)
    ItemCompraFormSet = inlineformset_factory(Compra, ItemCompra, form=ItemCompraForm, fk_name='numero_compra', extra=1, can_delete=True)
    form_itemcompra = ItemCompraFormSet(instance=instance_compra)

    if request.method == 'POST':
        form_compra = CompraForm(request.POST)

        if form_compra.is_valid():
            compra = form_compra.save(commit=False)
            form_itemcompra = ItemCompraFormSet(request.POST, request.FILES, instance=compra)

            if form_itemcompra.is_valid():
                compra.save()
                form_itemcompra.save()

                messages.success(request, 'Compra registrada com sucesso.', 'Sucesso')
                return redirect('list_compra')

            else:
                messages.error(request, form_itemcompra.errors, 'Erro itens de compra.')

        else:
            erro_compra = ''
            for erro in form_itemcompra.errors.values():
                erro_compra += '\n'
                erro_compra += erro[0]
            messages.error(request, erro_compra, 'Erro itens de compra.')

            return render(request, template, { 'form_compra' : form_compra, 'form_itemcompra': form_itemcompra })
    return render(request, template, { 'form_compra': CompraForm(instance=instance_compra), 'form_itemcompra': ItemCompraFormSet()})


@user_passes_test(check_gerente, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def update_compra(request, uuid):

    update_compra = Compra.objects.get(uuid=uuid)
    form_compra = CompraForm(instance=update_compra)
    ItemCompraFormSet = inlineformset_factory(Compra, ItemCompra, form=ItemCompraForm, fk_name='numero_compra', extra=1, can_delete=True)
    form_itemcompra = ItemCompraFormSet(instance=update_compra)

    if request.method == 'POST':
        form_compra = CompraForm(request.POST, instance=update_compra)

        if form_compra.is_valid():
            compra = form_compra.save(commit=False)
            form_itemcompra = ItemCompraFormSet(request.POST, request.FILES, instance=compra)

            if form_itemcompra.is_valid():
                compra.save()
                form_itemcompra.save()

                messages.success(request, 'Compra atualizado com sucesso.', 'Sucesso')
                return redirect('list_compra')
            else:
                messages.error(request, form_itemcompra.errors, 'Erro itens de compra.')

        else:
            erro_compra = ''
            for erro in form_compra.errors.values():
                erro_compra += '\n'
                erro_compra += erro[0]
            messages.error(request, erro_compra, 'Erro dados de compra.')

    return render(request, 'comercial/registrarcompra.html', { 'form_compra' : form_compra, 'form_itemcompra': form_itemcompra })


@user_passes_test(check_gerente, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def list_compra(request):
    template = 'comercial/gerenciarcompra.html'
    if request.method == 'POST':

        ordemcompra = request.POST.get('ordemcompra')
        dtordemcompra = request.POST.get('dtordemcompra')
        name_fornecedor = request.POST.get('fornecedor')
        status_compra = request.POST.get('status_compra')

        if ordemcompra != "":
            lista_compra = Compra.objects.filter(numero_compra=ordemcompra)
            if lista_compra.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif name_fornecedor != "":
            lista_compra = Compra.objects.filter(fornecedor__in=Fornecedor.objects.filter(fornecedorname__iexact=name_fornecedor))
            if lista_compra.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif dtordemcompra != "":
            lista_compra = Compra.objects.filter(data_compra__contains=dtordemcompra)
            if lista_compra.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif status_compra != "--Selecione--":
            lista_compra = Compra.objects.filter(status=status_compra)
            if lista_compra.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        else:
            messages.success(request, 'Nenhuma opção de pesquisa foi selecionada.', 'Erro')
            return render(request, template)
        return render(request, template, {'lista_compra': lista_compra})
    else:
        return render(request, template)



@login_required(login_url='/entrar')
def detalhes_compra(request, uuid):
    detalhes = ItemCompra.objects.filter(numero_compra=uuid)
    return render(request, "modal_listcompra.html", {'detalhes': detalhes})