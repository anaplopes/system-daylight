# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.clientemodel import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'clientename': forms.TextInput(attrs={'class':'form-control textcapitalize'}),
            'email': forms.EmailInput(attrs={'class':'form-control textlowercase'}),
            'numero_fiscal': forms.TextInput(attrs={'class':'form-control cpfcnpj'}),
            'endereco': forms.TextInput(attrs={'class':'form-control textcapitalize rua'}),
            'bairro': forms.TextInput(attrs={'class':'form-control textcapitalize bairro'}),
            'cidade': forms.TextInput(attrs={'class':'form-control textcapitalize cidade'}),
            'cep': forms.TextInput(attrs={'class':'form-control cep'}),
            'uf': forms.TextInput(attrs={'class':'form-control textuppercase uf'}),
            'telefone': forms.TextInput(attrs={'class':'form-control telefone'}),
            'class_fiscal': forms.Select(attrs={'class':'form-control class_fiscal'}),
            }
