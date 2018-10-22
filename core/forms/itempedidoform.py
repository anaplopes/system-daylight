# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.itempedidomodel import ItemPedido
from core.models.pedidomodel import Pedido


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = '__all__'
        exclude = ('numero_pedido',)

        widgets = {
            'produto': forms.Select(attrs={'class':'form-control'}),
            'produto': forms.Select(attrs={'class':'form-control'}),
            'cor': forms.Select(attrs={'class':'form-control'}),
            'tecido': forms.Select(attrs={'class':'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class':'form-control', 'id':'qtd_pedido'}),
            'valor_unitario': forms.NumberInput(attrs={'class':'form-control', 'id':'vlr_unit_pedido'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control', 'id':'total_item'}),
            }
