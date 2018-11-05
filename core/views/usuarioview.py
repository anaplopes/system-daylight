# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.usuarioform import CustomUserCreationForm, CustomUserChangeForm
from core.models.usuariomodel import CustomUser


@login_required(login_url='/entrar')
def create_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario cadastrado com sucesso.', 'Sucesso')
            return redirect('list_usuario')
        else:
            tipo_erro = ''
            for erro in form.errors.values():
                tipo_erro += '\n'
                tipo_erro += erro[0]
            messages.error(request, tipo_erro, 'Erro')
            return render(request, 'gerencial/cadastrarusuario.html', { 'form': form })
    return render(request, 'gerencial/cadastrarusuario.html', { 'form': CustomUserCreationForm() })


@login_required(login_url='/entrar')
def update_usuario(request, uuid):
    update_usuario = CustomUser.objects.get(uuid=uuid)
    form = CustomUserChangeForm(request.POST or None, instance=update_usuario)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produto atualizado com sucesso.', 'Sucesso')
        return redirect('list_usuario')
    else:
        tipo_erro = ''
        for erro in form.errors.values():
            tipo_erro += '\n'
            tipo_erro += erro[0]
        messages.error(request, tipo_erro, 'Erro')
    return render(request, 'gerencial/atualizarusuario.html', { 'form' : form, 'update_usuario':update_usuario })


@login_required(login_url='/entrar')
def delete_usuario(request, uuid):
    delete_usuario = Profile.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_usuario.delete()
        messages.success(request, 'Produto excluído com sucesso.', 'Sucesso')
        return redirect('list_usuario')
    return render(request, "exclusaoConf.html", {'delete_usuario': delete_usuario})


@login_required(login_url='/entrar')
def list_usuario(request):
    template = "gerencial/gerenciarusuario.html"
    if request.method == 'POST':

        nome_usuario = request.POST.get('nome_usuario')
        email_usuario = request.POST.get('email_usuario')
        cpf_usuario = request.POST.get('cpf_usuario')

        if cpf_usuario != "":
            lista_usuario = CustomUser.objects.filter(cpf=cpf_usuario)
        elif email_usuario != "":
            lista_usuario = CustomUser.objects.filter(email=email_usuario)
        elif nome_usuario != "":
            lista_usuario = CustomUser.objects.filter(nome__contains=nome_usuario)
        else:
            return render(request, template)
        return render(request, template, {'lista_usuario': lista_usuario})
    else:
        return render(request, template)
