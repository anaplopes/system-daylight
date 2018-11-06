# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.itemservicomodel import ItemServico
from core.models.servicomodel import Servico


class ItemServicoForm(forms.ModelForm):
    class Meta:
        model = ItemServico
        fields = '__all__'

        widgets = {
            'produto': forms.Select(attrs={'class':'form-control'}),
            'cor': forms.Select(attrs={'class':'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class':'form-control', 'id':'qtd_pedido'}),
            'valor_unitario': forms.NumberInput(attrs={'class':'form-control', 'id':'vlr_unit_pedido'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control', 'id':'total_item'}),
            }
