# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.materialform import MaterialForm
from core.models.materialmodel import Material


@login_required(login_url='/entrar')
def create_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        tipo_mprima = request.POST.get('tipo_mprima')
        if form.is_valid():
            form.save()
            messages.success(request, 'Material cadastrado com sucesso.')
            if tipo_mprima == 'Tecido' or tipo_mprima == 'tecido':
                return redirect('create_medida')
            else:
                return redirect('list_material')
        else:
            messages.error(request, form.errors)
            return render(request, 'comercial/cadastrarmaterial.html', { 'form' : form })
    return render(request, 'comercial/cadastrarmaterial.html', { 'form' : MaterialForm() })


@login_required(login_url='/entrar')
def update_material(request, uuid):
    update_material = Material.objects.get(uuid=uuid)
    form = MaterialForm(request.POST or None, instance=update_material)
    if form.is_valid():
        form.save()
        messages.success(request, 'Material atualizado com sucesso.')
        return redirect('list_material')
    else:
        messages.error(request, form.errors)
    return render(request, 'comercial/cadastrarmaterial.html', { 'form' : form, 'update_material':update_material })


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
        search = request.POST.get('cod_material')
        lista_material = Material.objects.filter(cod_mprima=search)
        if search == "":
            search = request.POST.get('tipo_material')
            lista_material = Material.objects.filter(tipo_mprima__contains=search)
            if search == "":
                search = request.POST.get('fabricante')
                lista_material = Material.objects.filter(nome_fabricante__contains=search)
                if search == "":
                    search = request.POST.get('desc_material')
                    lista_material = Material.objects.filter(material__contains=search)
                    if search == "":
                        return render(request, template)
        return render(request, template, {'lista_material':lista_material})
    else:
        return render(request, template)
