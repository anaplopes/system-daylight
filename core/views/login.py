# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


def login(request):
    template = 'registration/login.html'
    if request.method == 'POST':
        username=request.POST.get['username']
        password=request.POST.get['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            return HttpResponse('Invalid Login')
    else:
        return render(request, template)


def logout(request):
    logout(request)
    return redirect('login')
