# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.forms import formset_factory
from core.models.itempedidomodel import ItemPedido


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = '__all__'

        widgets = {
            'produto': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'cor': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'tecido': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'personalizacao': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'observacao': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'5'}),
            'quantidade': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'id':'qtd_pedido'}),
            'valor_unitario': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'id':'vlr_unit_pedido'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'id':'total_item'}),
            }
