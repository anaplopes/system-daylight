# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.clientemodel import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'clientename': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'numero_fiscal': forms.TextInput(attrs={'class':'form-control', 'id':'cpfcnpj'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
            'bairro': forms.TextInput(attrs={'class':'form-control'}),
            'cidade': forms.TextInput(attrs={'class':'form-control'}),
            'cep': forms.TextInput(attrs={'class':'form-control', 'id':'cep'}),
            'uf': forms.TextInput(attrs={'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'id':'telefone'}),
            'class_fiscal': forms.Select(attrs={'class':'form-control', 'id':'class_fiscal'}),
            }
