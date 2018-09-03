# -*- coding: utf-8 -*-
from django.http import HttpResponse
import django.contrib.messages as messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from core.forms import *
from core.models import *


def login(request):
    template = 'login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
            #return HttpResponse('Authenticated sucessfully')
        else:
            return HttpResponse('Invalid Login')
    else:
        return render(request, template)
