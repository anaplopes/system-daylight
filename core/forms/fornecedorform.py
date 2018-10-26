# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.fornecedormodel import Fornecedor


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

        widgets = {
            'fornecedorname': forms.TextInput(attrs={'class':'form-control'}),
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
