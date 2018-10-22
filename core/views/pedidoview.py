# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.pedidoform import PedidoForm
from core.models.pedidomodel import Pedido
from core.models.itempedidomodel import ItemPedido
from core.forms.itempedidoform import ItemPedidoForm
from django.forms import inlineformset_factory


@login_required(login_url='/entrar')
def register_pedido(request):
    template = 'comercial/registrarpedido.html'
    ItemPedidoFormSet = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)

    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST)
        form_item = ItemPedidoFormSet(request.POST, request.FILES)

        if form_pedido.is_valid() and form_item.is_valid():
            pedido = form_pedido.save()
            for f in form_item:
                itens = f.save(commit=False)
                itens.numero_pedido = pedido
                itens.save()
            messages.success(request, 'Pedido cadastrado com sucesso.')
            return redirect('list_pedido')
        else:
            return render(request, template, { 'form_pedido' : form_pedido, 'form_item': form_item })
    return render(request, template, { 'form_pedido': PedidoForm(), 'form_item': ItemPedidoFormSet()})


def list_pedido(request):
    template = 'comercial/gerenciarpedido.html'
    return render(request, template)
