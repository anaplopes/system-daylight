# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from core.forms.servicoform import ServicoForm
from core.models.servicomodel import Servico
from core.models.prestadormodel import PrestadorServico
from core.models.itemservicomodel import ItemServico
from core.forms.itemservicoform import ItemServicoForm
from django.forms import inlineformset_factory


@login_required(login_url='/entrar')
def register_servico(request):
    template = 'producao/registrarservico.html'

    instance_servico = Servico()
    form_servico = ServicoForm(instance=instance_servico)
    ItemServicoFormSet = inlineformset_factory(Servico, ItemServico, form=ItemServicoForm, fk_name='numero_servico', extra=1, can_delete=True)
    form_itemservico = ItemServicoFormSet(instance=instance_servico)

    if request.method == 'POST':
        form_servico = ServicoForm(request.POST)

        if form_servico.is_valid():
            servico = form_servico.save(commit=False)
            form_itemservico = ItemServicoFormSet(request.POST, request.FILES, instance=servico)

            if form_itemservico.is_valid():
                servico.save()
                form_itemservico.save()

                messages.success(request, 'Serviço registrado com sucesso.', 'Sucesso')
                return redirect('list_servico')
        else:
            tipo_erro1 = ''
            for erro in form_servico.errors.values():
                tipo_erro1 += '\n'
                tipo_erro1 += erro[0]
            messages.error(request, tipo_erro1, 'Erro dados de serviço.')

            tipo_erro2 = ''
            for erro in form_itemservico.errors.values():
                tipo_erro2 += '\n'
                tipo_erro2 += erro[0]
            messages.error(request, tipo_erro2, 'Erro itens de serviço.')

            return render(request, template, { 'form_servico' : form_servico, 'form_itemservico': form_itemservico })
    return render(request, template, { 'form_servico': ServicoForm(instance=instance_servico), 'form_itemservico': ItemServicoFormSet()})



@login_required(login_url='/entrar')
def update_servico(request, uuid):

    update_servico = Servico.objects.get(uuid=uuid)
    form_servico = ServicoForm(instance=update_servico)
    ItemServicoFormSet = inlineformset_factory(Servico, ItemServico, form=ItemServicoForm, fk_name='numero_servico', extra=0, can_delete=True)
    form_itemservico = ItemServicoFormSet(instance=update_servico)

    if request.method == 'POST':
        form_servico = ServicoForm(request.POST, instance=update_servico)

        if form_servico.is_valid():
            servico = form_servico.save(commit=False)
            form_itemservico = ItemServicoFormSet(request.POST, request.FILES, instance=servico)

            if form_itemservico.is_valid():
                servico.save()
                form_itemservico.save()

                messages.success(request, 'Serviço atualizado com sucesso.', 'Sucesso')
                return redirect('list_servico')

        else:
            tipo_erro1 = ''
            for erro in form_servico.errors.values():
                tipo_erro1 += '\n'
                tipo_erro1 += erro[0]
            messages.error(request, tipo_erro1, 'Erro dados de serviço.')

            tipo_erro2 = ''
            for erro in form_itemservico.errors.values():
                tipo_erro2 += '\n'
                tipo_erro2 += erro[0]
            messages.error(request, tipo_erro2, 'Erro itens de serviço.')
    return render(request, 'producao/registrarservico.html', { 'form_servico' : form_servico, 'form_itemservico': form_itemservico })


@login_required(login_url='/entrar')
def list_servico(request):
    template = 'producao/gerenciarservico.html'
    if request.method == 'POST':

        numservico = request.POST.get('numservico')
        dtservico = request.POST.get('dtservico')
        status_servico = request.POST.get('status_servico')
        name_prestador = request.POST.get('prestador')

        if numservico != "":
            lista_servico = Servico.objects.filter(numero_servico=numservico)
            if lista_servico.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif name_prestador != "":
            lista_servico = Servico.objects.filter(prestador__in=PrestadorServico.objects.filter(prestadorname__iexact=name_prestador))
            if lista_servico.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif dtservico != "":
            lista_servico = Servico.objects.filter(data_servico__contains=dtservico)
            if lista_servico.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        elif status_servico != "--Selecione--":
            lista_servico = Servico.objects.filter(status=status_servico)
            if lista_servico.count() == 0:
                messages.success(request, 'Sua pesquisa não retornou registros.', 'Informação')

        else:
            messages.success(request, 'Nenhuma opção de pesquisa foi selecionada.', 'Erro')
            return render(request, template)
        return render(request, template, {'lista_servico': lista_servico})
    else:
        return render(request, template)
