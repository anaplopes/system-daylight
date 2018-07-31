from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


def delete_usuario(request, id):
    delete_usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        delete_usuario.delete()
        return redirect('list_usuario')
    
    return render(request, "exclusaoConf.html", {'delete_usuario': delete_usuario})
