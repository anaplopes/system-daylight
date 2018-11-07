# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models.pedidomodel import Pedido
from core.models.servicomodel import Servico


@login_required(login_url='/entrar')
def expedicao(request):

    pronto_entrega = Servico.objects.filter(status='Finalizado')
    for entrega in pronto_entrega:
        pedido = entrega.numero_pedido
        confere = Servico.objects.filter(numero_pedido=pedido)
        if confere.count() == 1:
            lista_pedido = Pedido.objects.filter(numero_pedido=str(pedido)).order_by('data_entrega')
            
    x = lista_pedido
    return render(request, "expedicao.html", {'x': x})
