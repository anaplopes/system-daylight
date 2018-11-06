# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.compramodel import Compra


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

        widgets = {
            'fornecedor': forms.Select(attrs={'class':'form-control'}),
            'data_compra': forms.DateInput(attrs={'class':'form-control data'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control'}),
            'forma_pagamento': forms.Select(attrs={'class':'form-control'}),
            'prazo_pagamento': forms.Select(attrs={'class':'form-control'}),
            'responsavel': forms.TextInput(attrs={'class':'form-control textcapitalize'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'observacao': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'numero_pedido': forms.TextInput(attrs={'class':'form-control'}),
            'tecido': forms.Select(attrs={'class':'form-control'}),
            'qtd_tecido': forms.NumberInput(attrs={'class':'form-control'}),
            'valor_tecido': forms.NumberInput(attrs={'class':'form-control'}),
            'cor_tecido': forms.Select(attrs={'class':'form-control'}),
            }

