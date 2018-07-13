from django.shortcuts import render
from core.forms import *
from core.models import *


# Create your views here.

def home(request):
    return render(request, "index.html")



def login(request):
    return render(request, "login.html")



def grupoUsuario(request):
    context = {}
    template = "grupoUsuario.html"
    return render(request, template, context)

def usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(request, 'usuario.html', { "form" : form })



def grupoCliente(request):
    context = {}
    template = "grupoCliente.html"
    return render(request, template, context)

def cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'cliente.html', { "form" : form })



def grupoFornecedor(request):
    context = {}
    template = "grupoFornecedor.html"
    return render(request, template, context)

def fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FornecedorForm()
    return render(request, 'fornecedor.html', { "form" : form })



def grupoPrestador(request):
    context = {}
    template = "grupoPrestador.html"
    return render(request, template, context)

def prestador(request):
    if request.method == 'POST':
        form = PrestadorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PrestadorForm()
    return render(request, 'prestador.html', { "form" : form })


def grupoProduto(request):
    context = {}
    template = "grupoProduto.html"
    return render(request, template, context)

def produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProdutoForm()
    return render(request, 'produto.html', { "form" : form })



def grupoServico(request):
    context = {}
    template = "grupoServico.html"
    return render(request, template, context)

def servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ServicoForm()
    return render(request, 'servico.html', { "form" : form })


def grupoMaterial(request):
    context = {}
    template = "grupoMaterial.html"
    return render(request, template, context)

def material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MaterialForm()
    return render(request, 'material.html', { "form" : form })

def unidadeMedida(request):
    if request.method == 'POST':
        form = UnidadeMedidaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UnidadeMedidaForm()
    return render(request, 'unidadeMedida.html', { "form" : form })
