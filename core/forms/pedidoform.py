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

        widgets = {
            'numero_pedido': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'type':'hidden'}),
            'cliente': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'data_pedido': forms.DateInput(attrs={'class':'form-control form-control-sm data'}),
            'data_entrega': forms.DateInput(attrs={'class':'form-control form-control-sm data'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'readonly':'readonly'}),
            'forma_pagamento': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'prazo_pagamento': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'endereco_entrega': forms.TextInput(attrs={'class':'form-control form-control-sm textcapitalize'}),
            'solicitante': forms.TextInput(attrs={'class':'form-control form-control-sm textcapitalize'}),
            'status': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'personalizacao': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'observacao': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'3'}),
            }
