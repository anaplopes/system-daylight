# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.servicomodel import Servico
from core.models.itemservicomodel import ItemServico
from core.forms.itemservicoform import ItemServicoForm


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

        widgets = {
            'numero_servico': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'type':'hidden'}),
            'prestador': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'data_servico': forms.DateInput(attrs={'class':'form-control form-control-sm data'}),
            'data_entrega': forms.DateInput(attrs={'class':'form-control form-control-sm data'}),
            'tipo_servico': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'servico': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'status': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'readonly':'readonly'}),
            'observacao': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'3'}),
            'numero_pedido': forms.Select(attrs={'class':'form-control form-control-sm'}),
            }
