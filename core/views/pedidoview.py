# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.pedidoform import PedidoForm
from core.models.pedidomodel import Pedido
from core.models.clientemodel import Cliente
from core.models.itempedidomodel import ItemPedido
from core.forms.itempedidoform import ItemPedidoForm
from django.forms import inlineformset_factory
import datetime


@login_required(login_url='/entrar')
def register_pedido(request):
    template = 'comercial/registrarpedido.html'
   
    instance_pedido = Pedido()
    form_pedido = PedidoForm(instance=instance_pedido)
    ItemPedidoFormSet = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)

    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST)
        form_item = ItemPedidoFormSet(request.POST, request.FILES, prefix=fs_item)
        
        if form_pedido.is_valid():
            pedido = form_pedido.save(commit=False)
            form_item = ItemPedidoFormSet(request.POST, request.FILES, instance=pedido, prefix=fs_item)

            if form_item.is_valid():
                pedido.save()
                form_item.save()

                messages.success(request, 'Pedido cadastrado com sucesso.')
                return redirect('list_pedido')
        else:
            messages.error(request, form_pedido.errors)
            messages.error(request, form_item.errors)
            return render(request, template, { 'form_pedido' : form_pedido, 'form_item': form_item })
    return render(request, template, { 'form_pedido': PedidoForm(instance=instance_pedido), 'form_item': ItemPedidoFormSet()})


def list_pedido(request):
    template = 'comercial/gerenciarpedido.html'
    if request.method == 'POST':

        numpedido = request.POST.get('numpedido')
        dtentrega = request.POST.get('dtentrega')
        name_cliente = request.POST.get('cliente')

        if numpedido != "":
            lista_pedido = Pedido.objects.filter(numeropedido=numpedido)
        elif dtentrega != "":
            lista_pedido = Pedido.objects.filter(data_entrega__contains=dtentrega)
        elif name_cliente != "":
            lista_pedido = Pedido.objects.filter(cliente__in=Cliente.objects.filter(clientename__iexact=name_cliente))
        else:
            return render(request, template)
        return render(request, template, {'lista_pedido': lista_pedido})
    else:
        return render(request, template)
