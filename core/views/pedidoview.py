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


@login_required(login_url='/entrar')
def register_pedido(request):
    template = 'comercial/registrarpedido.html'
   
    instance_pedido = Pedido()
    form_pedido = PedidoForm(instance=instance_pedido)
    ItemPedidoFormSet = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)

    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST)
        form_itempedido = ItemPedidoFormSet(request.POST, request.FILES)
        
        if form_pedido.is_valid():
            pedido = form_pedido.save(commit=False)
            form_itempedido = ItemPedidoFormSet(request.POST, request.FILES, instance=pedido)

            if form_itempedido.is_valid():
                pedido.save()
                form_itempedido.save()

                messages.success(request, 'Pedido cadastrado com sucesso.')
                return redirect('list_pedido')
        else:
            messages.error(request, form_pedido.errors)
            messages.error(request, form_itempedido.errors)
            return render(request, template, { 'form_pedido' : form_pedido, 'form_itempedido': form_itempedido })
    return render(request, template, { 'form_pedido': PedidoForm(instance=instance_pedido), 'form_itempedido': ItemPedidoFormSet()})



@login_required(login_url='/entrar')
def update_pedido(request, uuid):
    ItemPedidoFormSet = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)
    update_pedido = Pedido.objects.get(uuid=uuid)
    form_pedido = PedidoForm(instance=update_pedido)
    form_itempedido = ItemPedidoFormSet(instance=update_pedido)

    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST, instance=update_pedido)

        if form_pedido.is_valid():
            pedido = form_pedido.save(commit=False)
            form_itempedido = ItemPedidoFormSet(request.POST, request.FILES, instance=pedido)
        
            if form_itempedido.is_valid():
                pedido.save()
                instances = form_itempedido.save(commit=False)
                for instance in instances:
                    instance.save()

                messages.success(request, 'Pedido atualizado com sucesso.')
                return redirect('list_pedido')
        else:
            messages.error(request, form_pedido.errors)
            messages.error(request, form_itempedido.errors)
    return render(request, 'comercial/registrarpedido.html', { 'form_pedido' : form_pedido, 'form_itempedido': form_itempedido, 'update_pedido':update_pedido })


@login_required(login_url='/entrar')
def list_pedido(request):
    template = 'comercial/gerenciarpedido.html'
    if request.method == 'POST':

        numpedido = request.POST.get('numpedido')
        dtcompra = request.POST.get('dtcompra')
        dtentrega = request.POST.get('dtentrega')
        name_cliente = request.POST.get('cliente')
        status_pedido = request.POST.get('status_pedido')

        if numpedido != "":
            lista_pedido = Pedido.objects.filter(numero_pedido=numpedido)
        elif name_cliente != "":
            lista_pedido = Pedido.objects.filter(cliente__in=Cliente.objects.filter(clientename__iexact=name_cliente))
        elif dtcompra != "":
            lista_pedido = Pedido.objects.filter(data_compra__contains=dtcompra)
        elif dtentrega != "":
            lista_pedido = Pedido.objects.filter(data_entrega__contains=dtentrega)
        elif status_pedido != "--Selecione--":
            lista_pedido = Pedido.objects.filter(status=status_pedido)
        else:
            return render(request, template)
        return render(request, template, {'lista_pedido': lista_pedido})
    else:
        return render(request, template)
