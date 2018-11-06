# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render




@login_required(login_url='/entrar')
def expedicao(request):
    return render(request, "expedicao.html")
