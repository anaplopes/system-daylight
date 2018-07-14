from django.shortcuts import render
from core.forms import *
from core.models import *


def login(request):
    return render(request, "login.html")
