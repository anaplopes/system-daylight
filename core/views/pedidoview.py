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
def register_pedido(request, uuid=None):
    template = 'comercial/registrarpedido.html'

    if uuid:
        pedido = Pedido.objects.get(uuid=uuid)
    else:
        pedido = Pedido()
    
    ItemPedidoFormSet = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=2)

    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST)
        form_item = ItemPedidoFormSet(request.POST, request.FILES, instance=pedido)

        if form_pedido.is_valid()and form_item.is_valid():
            form_pedido.save()
            form_item.save()
            messages.success(request, 'Pedido cadastrado com sucesso.')
            return redirect('list_pedido')
        else:
            return render(request, template, { 'form_pedido' : form_pedido, 'form_item': form_item })
    return render(request, template, { 'form_pedido': PedidoForm(), 'form_item': ItemPedidoFormSet()})


def list_pedido(request):
    template = 'comercial/gerenciarpedido.html'
    return render(request, template)
