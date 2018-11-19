# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from core.views.login import check_gerente
from django.contrib import messages
from django.shortcuts import render, redirect
from core.models.materialmodel import Material
from core.forms.materialform import MaterialForm


@user_passes_test(check_gerente, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def create_material(request):
    template = 'comercial/cadastrarmaterial.html'
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material cadastrado com sucesso.', 'Sucesso')
            return redirect('list_material')
        else:
            tipo_erro = ''
            for erro in form.errors.values():
                tipo_erro += '\n'
                tipo_erro += erro[0]
            messages.error(request, tipo_erro, 'Erro')
            return render(request, template, { 'form' : form })
    return render(request, template, { 'form' : MaterialForm() })


@user_passes_test(check_gerente, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def update_material(request, uuid):
    template = 'comercial/cadastrarmaterial.html'
    update_material = Material.objects.get(uuid=uuid)
    form = MaterialForm(request.POST or None, instance=update_material)
    if form.is_valid():
        form.save()
        messages.success(request, 'Material atualizado com sucesso.', 'Sucesso')
        return redirect('list_material')
    else:
        tipo_erro = ''
        for erro in form.errors.values():
            tipo_erro += '\n'
            tipo_erro += erro[0]
        messages.error(request, tipo_erro, 'Erro')
    return render(request, template, { 'form' : form, 'update_material':update_material })


'''
@login_required(login_url='/entrar')
def delete_material(request, uuid):
    delete_material = Material.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_material.delete()
        messages.success(request, 'Material excluído com sucesso.', 'Sucesso')
        return redirect('list_material')
    return render(request, "exclusaoConf.html", {'delete_material': delete_material})
'''


@user_passes_test(check_gerente, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def list_material(request):
    template = "comercial/gerenciarmaterial.html"
    if request.method == 'POST':

        material = request.POST.get('tipo_material')
        desc_material = request.POST.get('desc_material')

        if material != "":
            lista_material = Material.objects.filter(tipo_material__contains=material)
            if lista_material.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif desc_material != "":
            lista_material = Material.objects.filter(material__contains=desc_material)
            if lista_material.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        else:
            messages.success(request, 'Nenhuma opção de pesquisa foi selecionada.', 'Erro')
            return render(request, template)
        return render(request, template, {'lista_material': lista_material})
    else:
        return render(request, template)
