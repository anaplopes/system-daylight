from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


def create_usuario(request):
    form = UsuarioForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list_usuario')
    
    return render(request, 'cadastro/usuario.html', { 'form' : form })
