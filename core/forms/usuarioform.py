# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import Profile



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active',)

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
            }


    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = self.cleaned_data['is_staff']
        user.is_active = self.cleaned_data['is_active']
        
        if commit:
            user.save()
        return user



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nome', 'cpf', 'dt_nascimento', 'telefone', 'perfil',)

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{11}', 'title':'Somente numeros'}),
            'dt_nascimento': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'pattern':'\d{2}/\d{2}/\d{4}', 'title':'Data formato 00/00/0000'}),
            'telefone': forms.TextInput(attrs={'class':'form-control', 'pattern':'\d{11}', 'title':'FONE formato ddd + numero'}),
            'perfil': forms.Select(attrs={'class':'form-control'}),
            }


    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        profile.nome = self.cleaned_data['nome']
        profile.cpf = self.cleaned_data['cpf']
        profile.dt_nascimento = self.cleaned_data['dt_nascimento']
        profile.telefone = self.cleaned_data['telefone']
        profile.perfil = self.cleaned_data['perfil']
        
        if commit:
            profile.save()
        return profile
