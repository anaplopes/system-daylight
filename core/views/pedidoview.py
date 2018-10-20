# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.pedidoform import PedidoForm
from core.models.pedidomodel import Pedido
from core.forms.itempedidoform import ItemPedidoForm
from core.models.itempedidomodel import ItemPedido


@login_required(login_url='/entrar')
def register_pedido(request):
    template = 'comercial/registrarpedido.html'

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        form_item = ItemPedidoForm(request.POST)
        if form.is_valid() and form_item.is_valid():
            form.save()
            form_item.save()
            messages.success(request, 'Pedido cadastrado com sucesso.')
        else:
            messages.error(request, form.errors)
            return render(request, template, { 'form' : form, 'form_item': form_item })
    return render(request, template, { 'form': PedidoForm(), 'form_item': ItemPedidoForm()})


def list_pedido(request):
    template = 'comercial/gerenciarpedido.html'
    return render(request, template)