# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models.pedidomodel import Pedido
from core.models.compramodel import Compra
from core.models.servicomodel import Servico
import requests



@login_required(login_url='/entrar')
def index(request):
    data_agora = datetime.datetime.now()

    pedidos = Pedido.objects.filter(status='Em andamento')
    qtd_pedidos = len(pedidos)

    compras = Compra.objects.filter(status='Em andamento')
    qtd_compras = len(compras)

    servicos = Servico.objects.filter(status='Em andamento')
    qtd_servicos = len(servicos)

    expedicao = Servico.objects.filter(status='Finalizado')
    qtd_expedicao = len(expedicao)

    try:
        apiadvisor = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{id}/current?token={token}".format(id="3477", token="b7318a88ccb10c96eae3a3339bced184")
        temperatura = requests.api.get(apiadvisor).json()['data']['temperature']
        clima = requests.api.get(apiadvisor).json()['data']['condition']
        icone_previsao = requests.api.get(apiadvisor).json()['data']['icon']
        cidade = requests.api.get(apiadvisor).json()['name']
    except:
        pass

    return render(request, "index.html", { 'qtd_pedidos': qtd_pedidos,
                                            'qtd_compras': qtd_compras,
                                            'qtd_servicos': qtd_servicos,
                                            'qtd_expedicao': qtd_expedicao,
                                            'data_agora': data_agora,
                                            'temperatura': temperatura,
                                            'clima': clima,
                                            'icone_previsao': icone_previsao,
                                            'cidade': cidade })
