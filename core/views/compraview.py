# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.compraform import CompraForm
from core.models.compramodel import Compra
from core.models.fornecedormodel import Fornecedor
from core.models.itemcompramodel import ItemCompra
from core.forms.itemcompraform import ItemCompraForm
from django.forms import inlineformset_factory



@login_required(login_url='/entrar')
def register_compra(request):
    template = 'comercial/registrarcompra.html'

    instance_compra = Compra()
    form_compra = CompraForm(instance=instance_compra)
    ItemCompraFormSet = inlineformset_factory(Compra, ItemCompra, form=ItemCompraForm)

    if request.method == 'POST':
        form_compra = CompraForm(request.POST)
        form_itemcompra = ItemCompraFormSet(request.POST, request.FILES)

        if form_compra.is_valid():
            compra = form_compra.save(commit=False)
            form_itemcompra = ItemCompraFormSet(request.POST, request.FILES, instance=compra)

            if form_itemcompra.is_valid():
                compra.save()
                form_itemcompra.save()

                messages.success(request, 'Compra registrada com sucesso.', 'Sucesso')
                return redirect('list_compra')
        else:
            tipo_erro1 = ''
            for erro in form_compra.errors.values():
                tipo_erro1 += '\n'
                tipo_erro1 += erro[0]
            messages.error(request, tipo_erro1, 'Erro dados de compra.')

            return render(request, template, { 'form_compra' : form_compra, 'form_itemcompra': form_itemcompra })
    return render(request, template, { 'form_compra': CompraForm(instance=instance_compra), 'form_itemcompra': ItemCompraFormSet()})



@login_required(login_url='/entrar')
def update_compra(request, uuid):
    ItemCompraFormSet = inlineformset_factory(Compra, ItemCompra, form=ItemCompraForm)
    update_compra = Compra.objects.get(uuid=uuid)
    form_compra = CompraForm(instance=update_compra)
    form_itemcompra = ItemCompraFormSet(instance=update_compra)

    if request.method == 'POST':
        form_compra = CompraForm(request.POST, instance=update_compra)

        if form_compra.is_valid():
            compra = form_compra.save(commit=False)
            form_itemcompra = ItemCompraFormSet(request.POST, request.FILES, instance=compra)

            if form_itemcompra.is_valid():
                compra.save()
                instances = form_itemcompra.save(commit=False)
                for instance in instances:
                    instance.save()

                messages.success(request, 'Compra atualizado com sucesso.', 'Sucesso')
                return redirect('list_compra')
        else:
            tipo_erro1 = ''
            for erro in form_compra.errors.values():
                tipo_erro1 += '\n'
                tipo_erro1 += erro[0]
            messages.error(request, tipo_erro1, 'Erro dados de compra.')

            tipo_erro2 = ''
            for erro in form_itemcompra.errors.values():
                tipo_erro2 += '\n'
                tipo_erro2 += erro[0]
            messages.error(request, tipo_erro2, 'Erro itens de compra.')

    return render(request, 'comercial/registrarcompra.html', { 'form_compra' : form_compra, 'form_itemcompra': form_itemcompra, 'update_compra': update_compra })



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
        elif name_fornecedor != "":
            lista_compra = Compra.objects.filter(fornecedor__in=Fornecedor.objects.filter(fornecedorname__iexact=name_fornecedor))
        elif dtordemcompra != "":
            lista_compra = Compra.objects.filter(data_compra__contains=dtordemcompra)
        elif status_compra != "--Selecione--":
            lista_compra = Compra.objects.filter(status=status_compra)
        else:
            return render(request, template)
        return render(request, template, {'lista_compra': lista_compra})
    else:
        return render(request, template)
