# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.medidamodel import UnidadeMedida


class UnidadeMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadeMedida
        fields = '__all__'

        widgets = {
            'tecido': forms.Select(attrs={'class':'form-control'}),
            'produto': forms.Select(attrs={'class':'form-control'}),
            'qtd_unidade': forms.NumberInput(attrs={'class':'form-control'}),
            }
