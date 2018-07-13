# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.servico import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

        widgets = {
            'tipo_servico': forms.Select(attrs={'class':'form-control'}),
            'servico': forms.Select(attrs={'class':'form-control'}),
            'tipo_produto': forms.Select(attrs={'class':'form-control'}),
            'valor_peca': forms.NumberInput(attrs={'class':'form-control'}),
            }
