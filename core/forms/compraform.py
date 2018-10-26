# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.compramodel import Compra


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        exclude = ('numero_compra',)

        widgets = {
            'fornecedor': forms.Select(attrs={'class':'form-control'}),
            'data_compra': forms.DateInput(attrs={'class':'form-control', 'id':'datacompra'}),
            'data_entrega': forms.DateInput(attrs={'class':'form-control', 'id':'dataentrega'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control', 'id':'total_pedido'}),
            'forma_pagamento': forms.Select(attrs={'class':'form-control'}),
            'prazo_pagamento': forms.Select(attrs={'class':'form-control'}),
            'responsavel': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'observacao': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            }

