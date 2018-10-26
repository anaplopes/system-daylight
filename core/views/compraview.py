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
import datetime



@login_required(login_url='/entrar')
def register_compra(request):
    template = 'comercial/registrarcompra.html'
   
    instance_compra = Compra()
    form_compra = CompraForm(instance=instance_compra)
    ItemCompraFormSet = inlineformset_factory(Compra, ItemCompra, form=ItemCompraForm, extra=1)

    if request.method == 'POST':
        form_compra = CompraForm(request.POST)
        form_item = ItemCompraFormSet(request.POST, request.FILES)
        
        if form_compra.is_valid():
            compra = form_compra.save(commit=False)
            form_item = ItemCompraFormSet(request.POST, request.FILES, instance=compra)

            if form_item.is_valid():
                compra.save()
                form_item.save()

                messages.success(request, 'Compra cadastrada com sucesso.')
                return redirect('list_compra')
        else:
            messages.error(request, form_compra.errors)
            messages.error(request, form_item.errors)
            return render(request, template, { 'form_compra' : form_compra, 'form_item': form_item })
    return render(request, template, { 'form_compra': CompraForm(instance=instance_compra), 'form_item': ItemCompraFormSet()})



@login_required(login_url='/entrar')
def update_compra(request, uuid):
    update_compra = Compra.objects.get(uuid=uuid)
    form = CompraForm(request.POST or None, instance=update_compra)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pedido atualizado com sucesso.')
        return redirect('list_compra')
    else:
        messages.error(request, form.errors)
    return render(request, 'comercial/registrarcompra.html', { 'form' : form, 'update_compra':update_compra })   


@login_required(login_url='/entrar')
def list_compra(request):
    template = 'comercial/gerenciarcompra.html'
    if request.method == 'POST':

        numero_pedido = request.POST.get('numero_pedido')
        data_compra = request.POST.get('data_compra')
        fornecedor = request.POST.get('fornecedor')

        if numero_pedido != "":
            lista_compra = Compra.objects.filter(numero_pedido=numero_pedido)
        elif fornecedor != "":
            lista_compra = Compra.objects.filter(fornecedor__in=Fornecedor.objects.filter(fornecedor__iexact=fornecedor))
        elif data_compra != "":
            lista_compra = Compra.objects.filter(data_entrega__contains=data_entrega)
        else:
            return render(request, template)
        return render(request, template, {'lista_compra': lista_compra})
    else:
        return render(request, template) 



