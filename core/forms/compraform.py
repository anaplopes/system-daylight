# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.compramodel import Compra
from core.models.itemcompramodel import ItemCompra
from core.forms.itemcompraform import ItemCompraForm


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

        widgets = {
            'numero_compra': forms.NumberInput(attrs={'class':'form-control form-control-sm', 'type':'hidden'}),
            'fornecedor': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'data_compra': forms.DateInput(attrs={'class':'form-control form-control-sm data'}),
            'valor_total': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'forma_pagamento': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'prazo_pagamento': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'responsavel': forms.TextInput(attrs={'class':'form-control form-control-sm textcapitalize'}),
            'status': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'observacao': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'3'}),
            'numero_pedido': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'tecido': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'qtd_tecido': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'valor_tecido': forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'cor_tecido': forms.Select(attrs={'class':'form-control form-control-sm'}),
            }

