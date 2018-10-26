# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.pedidomodel import Pedido
from core.models.itempedidomodel import ItemPedido
from core.forms.itempedidoform import ItemPedidoForm


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ('numero_pedido',)

        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'data_compra': forms.DateInput(attrs={'class':'form-control', 'id':'datacompra'}),
            'data_entrega': forms.DateInput(attrs={'class':'form-control', 'id':'dataentrega'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control', 'id':'total_pedido'}),
            'forma_pagamento': forms.Select(attrs={'class':'form-control'}),
            'prazo_pagamento': forms.Select(attrs={'class':'form-control'}),
            'endereco_entrega': forms.TextInput(attrs={'class':'form-control'}),
            'solicitante': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'personalizacao': forms.Select(attrs={'class':'form-control'}),
            'observacao': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            }
