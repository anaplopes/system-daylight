# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'is_staff', 'is_active', 'nome', 'cpf', 
        'dt_nascimento', 'telefone', 'perfil', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{11}', 'title':'Somente numeros'}),
            'dt_nascimento': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'pattern':'\d{2}/\d{2}/\d{4}', 'title':'Data formato 00/00/0000'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{11}', 'title':'FONE formato ddd + numero'}),
            'perfil': forms.Select(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
            }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_staff', 'is_active', 'nome', 'cpf', 
        'dt_nascimento', 'telefone', 'perfil')

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{11}', 'title':'Somente numeros'}),
            'dt_nascimento': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'pattern':'\d{2}/\d{2}/\d{4}', 'title':'Data formato 00/00/0000'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{11}', 'title':'FONE formato ddd + numero'}),
            'perfil': forms.Select(attrs={'class':'form-control'}),
            }
