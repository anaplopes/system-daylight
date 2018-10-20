# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.tecidomodel import Tecido


class TecidoForm(forms.ModelForm):
    class Meta:
        model = Tecido
        fields = '__all__'

        widgets = {
            'tecido': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_tecido': forms.Select(attrs={'class':'form-control'}),
            'nome_fabricante': forms.TextInput(attrs={'class':'form-control'}),
            }
