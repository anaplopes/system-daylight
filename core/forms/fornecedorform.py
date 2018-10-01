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
            'numero_fiscal': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{14}', 'title':'Somente numeros'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
            'bairro': forms.TextInput(attrs={'class':'form-control'}),
            'cidade': forms.TextInput(attrs={'class':'form-control'}),
            'cep': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{5}-\d{3}', 'title':'CEP formato 00000-000'}),
            'uf': forms.TextInput(attrs={'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{11}', 'title':'FONE formato ddd + numero'}),
            'class_fiscal': forms.Select(attrs={'class':'form-control'}),
            }
