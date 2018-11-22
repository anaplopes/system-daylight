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
            'numero_compra': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'type':'hidden'}),
            'tecido': forms.Select(attrs={'class':'form-control form-control-sm', 'onchange':'disableTecido()'}),
            'material': forms.Select(attrs={'class':'form-control form-control-sm', 'onchange':'disableMaterial()'}),
            'cor': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'quantidade': forms.NumberInput(attrs={'class':'form-control form-control-sm qtd', 'onchange':'calcTotalCompra()'}),
            'valor_unitario': forms.NumberInput(attrs={'class':'form-control form-control-sm vlr_unitario', 'onchange':'calcTotalCompra()'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control form-control-sm totalitem', 'readonly':'readonly'}),
            }
