# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect
from core.views.login import check_gerente
from core.forms.usuarioform import CustomUserCreationForm, CustomUserChangeForm
from core.models.usuariomodel import CustomUser



@user_passes_test(check_gerente, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def create_usuario(request):
    template = 'gerencial/cadastrarusuario.html'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso.', 'Sucesso')
            return redirect('list_usuario')
        else:
            tipo_erro = ''
            for erro in form.errors.values():
                tipo_erro += '\n'
                tipo_erro += erro[0]
            messages.error(request, tipo_erro, 'Erro')
            return render(request, template, { 'form':form })
    return render(request, template, { 'form': CustomUserCreationForm() })


@user_passes_test(check_gerente, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def update_usuario(request, uuid):
    update_usuario = CustomUser.objects.get(uuid=uuid)
    form = CustomUserChangeForm(request.POST or None, instance=update_usuario)
    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário atualizado com sucesso.', 'Sucesso')
        return redirect('list_usuario')
    else:
        tipo_erro = ''
        for erro in form.errors.values():
            tipo_erro += '\n'
            tipo_erro += erro[0]
        messages.error(request, tipo_erro, 'Erro')
    return render(request, 'gerencial/atualizarusuario.html', { 'form':form, 'update_usuario':update_usuario })


'''
@login_required(login_url='/entrar')
def delete_usuario(request, uuid):
    delete_usuario = Profile.objects.get(uuid=uuid)
    if request.method == 'POST':
        delete_usuario.delete()
        messages.success(request, 'Usuário excluído com sucesso.', 'Sucesso')
        return redirect('list_usuario')
    return render(request, "exclusaoConf.html", {'delete_usuario': delete_usuario})
'''


@user_passes_test(check_gerente, login_url='/?error=acesso', redirect_field_name=None)
@login_required(login_url='/entrar')
def list_usuario(request):
    template = "gerencial/gerenciarusuario.html"
    if request.method == 'POST':

        nome_usuario = request.POST.get('nome_usuario')
        email_usuario = request.POST.get('email_usuario')
        cpf_usuario = request.POST.get('cpf_usuario')

        if cpf_usuario != "":
            lista_usuario = CustomUser.objects.filter(cpf=cpf_usuario)
            if lista_usuario.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif email_usuario != "":
            lista_usuario = CustomUser.objects.filter(email=email_usuario)
            if lista_usuario.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif nome_usuario != "":
            lista_usuario = CustomUser.objects.filter(nome__contains=nome_usuario)
            if lista_usuario.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        else:
            messages.success(request, 'Nenhuma opção de pesquisa foi selecionada.', 'Erro')
            return render(request, template)
        return render(request, template, {'lista_usuario':lista_usuario})
    else:
        return render(request, template)


@login_required(login_url='/entrar')
def password_change(request):
    template = 'registration/password_change.html'
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST or None)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso.', 'Sucesso')
            return redirect('home')
        else:
            tipo_erro = ''
            for erro in form.errors.values():
                tipo_erro += '\n'
                tipo_erro += erro[0]
            messages.error(request, tipo_erro, 'Erro')
            return redirect('home')
        return render(request, template, { 'form':form })
    return render(request, template, {'form': PasswordChangeForm(request.user)})
