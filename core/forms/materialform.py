# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from core.models.materialmodel import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

        widgets = {
            'material': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_material': forms.Select(attrs={'class':'form-control'}),
            'Subtipo_material': forms.Select(attrs={'class':'form-control'}),
            }
