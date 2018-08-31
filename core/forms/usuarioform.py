# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.usuario import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{11}', 'title':'Somente numeros'}),
            'dt_nascimento': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'pattern':'\d{2}/\d{2}/\d{4}', 'title':'Data formato 00/00/0000'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{11}', 'title':'FONE formato ddd + numero'}),
            'perfil': forms.Select(attrs={'class':'form-control'}),
            'status_user': forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'is_staff': forms.NullBooleanSelect(attrs={'class':'form-control'}),
        }
