# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.itemcompramodel import ItemCompra
from core.models.compramodel import Compra


class ItemCompraForm(forms.ModelForm):
    class Meta:
        model = ItemCompra
        fields = '__all__'

        widgets = {
            'material': forms.Select(attrs={'class':'form-control'}),
            'cor': forms.Select(attrs={'class':'form-control'}),
           # 'tecido': forms.Select(attrs={'class':'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class':'form-control', 'id':'qtd_pedido'}),
            'valor_unitario': forms.NumberInput(attrs={'class':'form-control', 'id':'vlr_unit_pedido'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control', 'id':'total_item'}),
            }
