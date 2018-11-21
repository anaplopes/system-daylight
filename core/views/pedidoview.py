# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from core.views.login import check_multiuser_v
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.pedidoform import PedidoForm
from core.models.pedidomodel import Pedido
from core.models.clientemodel import Cliente
from core.models.itempedidomodel import ItemPedido
from core.forms.itempedidoform import ItemPedidoForm
from django.forms import inlineformset_factory


@user_passes_test(check_multiuser_v, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def register_pedido(request):
    template = 'comercial/registrarpedido.html'

    instance_pedido = Pedido()
    form_pedido = PedidoForm(instance=instance_pedido)
    ItemPedidoFormSet = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, fk_name='numero_pedido', extra=1, can_delete=True)
    form_itempedido = ItemPedidoFormSet(instance=instance_pedido)

    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST)

        if form_pedido.is_valid():
            pedido = form_pedido.save(commit=False)
            form_itempedido = ItemPedidoFormSet(request.POST, request.FILES, instance=pedido)

            if form_itempedido.is_valid():
                pedido.save()
                form_itempedido.save()
                
                messages.success(request, 'Pedido registrado com sucesso.', 'Sucesso')
                return redirect('list_pedido')

        else:
            tipo_erro1 = ''
            for erro in form_pedido.errors.values():
                tipo_erro1 += '\n'
                tipo_erro1 += erro[0]
            messages.error(request, tipo_erro1, 'Erro dados de pedido.')

            tipo_erro2 = ''
            for erro in form_itempedido.errors.values():
                tipo_erro2 += '\n'
                tipo_erro2 += erro[0]
            messages.error(request, tipo_erro2, 'Erro itens de pedido.')

            return render(request, template, { 'form_pedido' : form_pedido, 'form_itempedido': form_itempedido })
    return render(request, template, { 'form_pedido': PedidoForm(instance=instance_pedido), 'form_itempedido': ItemPedidoFormSet()})


@user_passes_test(check_multiuser_v, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def update_pedido(request, uuid):

    update_pedido = Pedido.objects.get(uuid=uuid)
    form_pedido = PedidoForm(instance=update_pedido)
    ItemPedidoFormSet = inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, fk_name='numero_pedido', extra=1, can_delete=True)
    form_itempedido = ItemPedidoFormSet(instance=update_pedido)

    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST, instance=update_pedido)

        if form_pedido.is_valid():
            pedido = form_pedido.save(commit=False)
            form_itempedido = ItemPedidoFormSet(request.POST, request.FILES, instance=pedido)

            if form_itempedido.is_valid():
                pedido.save()
                form_itempedido.save()

                messages.success(request, 'Pedido atualizado com sucesso.', 'Sucesso')
                return redirect('list_pedido')

        else:
            tipo_erro1 = ''
            for erro in form_pedido.errors.values():
                tipo_erro1 += '\n'
                tipo_erro1 += erro[0]
            messages.error(request, tipo_erro1, 'Erro dados de pedido.')

            tipo_erro2 = ''
            for erro in form_itempedido.errors.values():
                tipo_erro2 += '\n'
                tipo_erro2 += erro[0]
            messages.error(request, tipo_erro2, 'Erro itens de pedido.')
    return render(request, 'comercial/registrarpedido.html', {'form_pedido': form_pedido, 'form_itempedido': form_itempedido})


@user_passes_test(check_multiuser_v, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def list_pedido(request):
    template = 'comercial/gerenciarpedido.html'
    if request.method == 'POST':

        numpedido = request.POST.get('numpedido')
        dtpedido = request.POST.get('dtpedido')
        dtentrega = request.POST.get('dtentrega')
        name_cliente = request.POST.get('cliente')
        status_pedido = request.POST.get('status_pedido')

        if numpedido != "":
            lista_pedido = Pedido.objects.filter(numero_pedido=numpedido)
            if lista_pedido.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif name_cliente != "":
            lista_pedido = Pedido.objects.filter(cliente__in=Cliente.objects.filter(clientename__iexact=name_cliente))
            if lista_pedido.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif dtpedido != "":
            lista_pedido = Pedido.objects.filter(data_pedido__contains=dtpedido)
            if lista_pedido.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif dtentrega != "":
            lista_pedido = Pedido.objects.filter(data_entrega__contains=dtentrega)
            if lista_pedido.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif status_pedido != "--Selecione--":
            lista_pedido = Pedido.objects.filter(status=status_pedido)
            if lista_pedido.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        else:
            messages.success(request, 'Nenhuma opção de pesquisa foi selecionada.', 'Erro')
            return render(request, template)
        return render(request, template, {'lista_pedido': lista_pedido})
    else:
        return render(request, template)



@login_required(login_url='/entrar')
def detalhes_pedido(request, uuid):
    detalhes = ItemPedido.objects.filter(numero_pedido=uuid)
    return render(request, "modal_listpedido.html", {'detalhes': detalhes})