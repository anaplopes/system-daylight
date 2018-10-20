# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.produtomodel import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        widgets = {
            'tipo_produto': forms.Select(attrs={'class':'form-control'}),
            'produto': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.Select(attrs={'class':'form-control'}),
            'classificacao': forms.Select(attrs={'class':'form-control'}),
            'tamanho': forms.Select(attrs={'class':'form-control'}),
            }
