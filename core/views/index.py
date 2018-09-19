# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.forms import *
from core.models import *


@login_required(login_url='/entrar')
def index(request):
    return render(request, "index.html")
