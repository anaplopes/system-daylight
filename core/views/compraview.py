# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.compraform import CompraForm
from core.models.compramodel import Compra
from core.models.itemcompramodel import ItemCompra
from core.forms.itemcompraform import ItemCompraForm
from django.forms import inlineformset_factory



@login_required(login_url='/entrar')
def register_compra(request, uuid=None):
    template = 'comercial/registrarcompra.html'

    if uuid:
        compra = Compra.objects.get(uuid=uuid)
    else:
        compra = Compra()
    
    ItemCompraFormSet = inlineformset_factory(Compra, ItemCompra, form=ItemCompraForm, extra=2)

    if request.method == 'POST':
        form_compra = CompraForm(request.POST)
        form_item = ItemCompraFormSet(request.POST, request.FILES, instance=compra)

        if form_compra.is_valid()and form_item.is_valid():
            form_compra.save()
            form_item.save()
            messages.success(request, 'Pedido cadastrado com sucesso.')
            return redirect('list_compra')
        else:
            return render(request, template, { 'form_compra' : form_compra, 'form_item': form_item })
    return render(request, template, { 'form_compra': CompraForm(), 'form_item': ItemCompraFormSet()})


def list_compra(request):
    template = 'comercial/gerenciarcompra.html'
    return render(request, template)
