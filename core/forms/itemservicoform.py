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
            'numero_servico': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'type':'hidden'}),
            'produto': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'cor': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'quantidade': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'valor_unitario': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            }
