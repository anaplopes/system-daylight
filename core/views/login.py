# -*- coding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse
import django.contrib.messages as messages
from django.shortcuts import render
from core.forms import *
from core.models import *


class AcessoView(View):
    def login(self):
        context = {}
        next = self.GET.get('next')
        if self.method == 'POST':
            username = self.POST.get('email')
            senha = self.POST.get('password')
            usuario = authenticate(username=username, password=senha)

            if usuario is not None:
                login(self, usuario)
                if next:
                    return redirect(next)
                return redirect('home')

            messages.error(self, 'Login e senha não encontrados. Tente logar novamente!', "Login inválido")
            return redirect('login')
        template = 'login.html'
        return HttpResponse(template.render(context, self))
    
    
    def logout(self):
        logout(self)
        return redirect('login')
    
