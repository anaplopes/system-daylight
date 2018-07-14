from django.shortcuts import render
from core.forms import *
from core.models import *


def home(request):
    return render(request, "index.html")
