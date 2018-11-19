# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


def login(request):
    template = 'registration/login.html'
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                return redirect('home')
        else:
            return HttpResponse('Invalid Login')
    else:
        return render(request, template)


def logout(request):
    logout(request)
    return redirect('login')


def check_gerente(user):
    return user.perfil == 'G'


def check_vendedor(user):
    return user.perfil == 'V'


def check_assistente(user):
    return user.perfil == 'A'


def check_multiuser_v(user):
    if user.perfil == 'G' or user.perfil == 'V':
        return 'MV'


def check_multiuser_a(user):
    if user.perfil == 'G' or user.perfil == 'A':
        return 'MA'