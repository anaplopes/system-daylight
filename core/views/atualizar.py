from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


@login_required(login_url='/login/')
def update_usuario(request, id):
    update_usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST or None, instance=update_usuario)
    if form.is_valid():
        form.save()
        return redirect('list_usuario')
    return render(request, 'gerencial/cadastrarusuario.html', { 'form' : form, 'update_usuario':update_usuario })


@login_required(login_url='/login/')
def update_cliente(request, id):
    update_cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=update_cliente)
    if form.is_valid():
        form.save()
        return redirect('list_cliente')
    return render(request, 'comercial/cadastrarcliente.html', { 'form' : form, 'update_cliente':update_cliente })


@login_required(login_url='/login/')
def update_fornecedor(request, id):
    update_fornecedor = Fornecedor.objects.get(id=id)
    form = FornecedorForm(request.POST or None, instance=update_fornecedor)
    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')
    return render(request, 'comercial/cadastrarfornecedor.html', { 'form' : form, 'update_fornecedor':update_fornecedor })


@login_required(login_url='/login/')
def update_prestador(request, id):
    update_prestador = PrestadorServico.objects.get(id=id)
    form = PrestadorForm(request.POST or None, instance=update_prestador)
    if form.is_valid():
        form.save()
        return redirect('list_prestador')
    return render(request, 'producao/cadastrarprestador.html', { 'form' : form, 'update_prestador':update_prestador })


@login_required(login_url='/login/')
def update_material(request, id):
    update_material = Material.objects.get(id=id)
    form = MaterialForm(request.POST or None, instance=update_material)
    if form.is_valid():
        form.save()
        return redirect('list_material')
    return render(request, 'comercial/cadastrarmaterial.html', { 'form' : form, 'update_material':update_material })


@login_required(login_url='/login/')
def update_medida(request, id):
    update_medida = UnidadeMedida.objects.get(id=id)
    form = UnidadeMedidaForm(request.POST or None, instance=update_medida)
    if form.is_valid():
        form.save()
        return redirect('create_medida')
    return render(request, 'comercial/cadastrarmedida.html', { 'form' : form, 'update_medida':update_medida })


@login_required(login_url='/login/')
def update_produto(request, id):
    update_produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=update_produto)
    if form.is_valid():
        form.save()
        return redirect('list_produto')
    return render(request, 'comercial/cadastrarproduto.html', { 'form' : form, 'update_produto':update_produto })


@login_required(login_url='/login/')
def update_servico(request, id):
    update_servico = Servico.objects.get(id=id)
    form = ServicoForm(request.POST or None, instance=update_servico)
    if form.is_valid():
        form.save()
        return redirect('list_servico')
    return render(request, 'producao/cadastrarservico.html', { 'form' : form, 'update_servico':update_servico })
