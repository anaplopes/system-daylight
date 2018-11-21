# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.itempedidomodel import ItemPedido
from core.models.pedidomodel import Pedido


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = '__all__'

        widgets = {
            'numero_pedido': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'type':'hidden'}),
            'produto': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'cor': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'tecido': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'quantidade': forms.NumberInput(attrs={'class':'form-control form-control-sm qtd', 'onchange':'calcTotalPedido()'}),
            'valor_unitario': forms.NumberInput(attrs={'class':'form-control form-control-sm vlr_unitario', 'onchange':'calcTotalPedido()'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control form-control-sm totalitem'}),
            }
