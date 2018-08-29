from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.forms import *
from core.models import *

@login_required(login_url='/acesso/login')
def home(request):
    return render(request, "index.html")
