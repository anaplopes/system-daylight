# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.servicomodel import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

        widgets = {
            'prestador': forms.Select(attrs={'class':'form-control'}),
            'data_servico': forms.DateInput(attrs={'class':'form-control data'}),
            'data_entrega': forms.DateInput(attrs={'class':'form-control data'}),
            'tipo_servico': forms.Select(attrs={'class':'form-control'}),
            'servico': forms.Select(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control', 'id':'total_pedido'}),
            'observacao': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'numero_pedido': forms.Select(attrs={'class':'form-control'}),
            }
