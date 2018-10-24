# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.models.materialmodel import Material
from core.forms.materialform import MaterialForm


@login_required(login_url='/entrar')
def create_material(request):
    template = 'comercial/cadastrarmaterial.html'
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material cadastrado com sucesso.')
            return redirect('list_material')
        else:
            messages.error(request, form.errors)
            return render(request, template, { 'form' : form })
    return render(request, template, { 'form' : MaterialForm() })


@login_required(login_url='/entrar')
def update_material(request, uuid):
    template = 'comercial/cadastrarmaterial.html'
    update_material = Material.objects.get(uuid=uuid)
    form = MaterialForm(request.POST or None, instance=update_material)
    if form.is_valid():
        form.save()
        messages.success(request, 'Material atualizado com sucesso.')
        return redirect('list_material')
    else:
        messages.error(request, form.errors)
    return render(request, template, { 'form' : form, 'update_material':update_material })


@login_required(login_url='/entrar')
def delete_material(request, uuid):
    delete_material = Material.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_material.delete()
        messages.success(request, 'Material excluído com sucesso.')
        return redirect('list_material')
    return render(request, "exclusaoConf.html", {'delete_material': delete_material})


@login_required(login_url='/entrar')
def list_material(request):
    template = "comercial/gerenciarmaterial.html"
    if request.method == 'POST':
        
        material = request.POST.get('tipo_material')
        desc_material = request.POST.get('desc_material')

        if material != "":
            lista_material = Material.objects.filter(tipo_material__contains=material)
        elif desc_material != "":
            lista_material = Material.objects.filter(material__contains=desc_material)
        else:
            return render(request, template)
        return render(request, template, {'lista_material': lista_material})
    else:
        return render(request, template)
