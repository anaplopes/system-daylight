# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from core.models.pedidomodel import Pedido
from core.models.servicomodel import Servico


@login_required(login_url='/entrar')
def expedicao(request):
    data_hj = datetime.date.today()
        
    pedido_entregue = None
    pronto_entrega = {}

    # lista os pedidos disponiveis para entrega
    validacao_status = []
    
    serv_finalizado = Servico.objects.filter(status='Finalizado')
    for entrega in serv_finalizado:
        pedido = entrega.numero_pedido
        
        qtd = Servico.objects.filter(numero_pedido=pedido).count()
        if qtd >= 1:
            confere = Servico.objects.filter(numero_pedido=pedido)
            for obj_confere in confere:
                if obj_confere.status == 'Finalizado':
                    validacao_status.append('ok')
                else:
                    validacao_status.append('erro')
                    
                    
        if 'erro' in validacao_status:
            validacao_status.clear()
            
        else:
            validacao_status.clear()
            lista_pedido = Pedido.objects.filter(numero_pedido=str(pedido)).order_by('data_entrega')
            for item in lista_pedido:
                if item.status == 'Em andamento':
                    pronto_entrega[pedido] = lista_pedido


    # finaliza o pedido apos a entrega
    if request.method == 'POST':
        uuid_pedido = request.POST.getlist('lista[]')
        for uuid in uuid_pedido:
            pedido_entregue = Pedido.objects.get(uuid=uuid)
            pedido_entregue.status = 'Finalizado'
            pedido_entregue.data_entrega = data_hj
            pedido_entregue.save()
        messages.success(request, 'Pedido finalizado.', 'Sucesso')
        
    return render(request, "expedicao.html", {'pronto_entrega': pronto_entrega, 'pedido_entregue': pedido_entregue})
