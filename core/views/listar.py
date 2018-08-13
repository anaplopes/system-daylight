from django.shortcuts import render
from core.forms import *
from core.models import *


def list_usuario(request):
    if request.method == 'POST':

        search = request.POST.get('nome_usuario')
        lista_usuario = Usuario.objects.filter(nome__contains=search)

        if search == "":
            search = request.POST.get('email_usuario')
            lista_usuario = Usuario.objects.filter(email__contains=search)

            if search == "":
                search = request.POST.get('cpf_usuario')
                lista_usuario = Usuario.objects.filter(cpf=search)

                if search == "":
                    return render(request, "grupo/grupousuario.html")

        return render(request, "grupo/grupousuario.html", {'lista_usuario':lista_usuario})
    else:
        return render(request, "grupo/grupousuario.html")


def list_cliente(request):
    if request.method == 'POST':
        
        search = request.POST.get('nome_cliente')
        lista_cliente = Cliente.objects.filter(clientename__contains=search)

        if search == "":
            search = request.POST.get('email_cliente')
            lista_cliente = Cliente.objects.filter(email__contains=search)

            if search == "":
                search = request.POST.get('cpf/cnpj_cliente')
                lista_cliente = Cliente.objects.filter(numero_fiscal=search)

                if search == "":
                    return render(request, "grupo/grupocliente.html")

        return render(request, "grupo/grupocliente.html", {'lista_cliente':lista_cliente})
    else:
        return render(request, "grupo/grupocliente.html")
   

def list_fornecedor(request):
    if request.method == 'POST':
        
        search = request.POST.get('nome_fornecedor')
        lista_fornecedor = Fornecedor.objects.filter(fornecedorname__contains=search)

        if search == "":
            search = request.POST.get('email_fornecedor')
            lista_fornecedor = Fornecedor.objects.filter(email__contains=search)

            if search == "":
                search = request.POST.get('cpf/cnpj_fornecedor')
                lista_fornecedor = Fornecedor.objects.filter(numero_fiscal=search)

                if search == "":
                    return render(request, "grupo/grupofornecedor.html")

        return render(request, "grupo/grupofornecedor.html", {'lista_fornecedor':lista_fornecedor})
    else:
        return render(request, "grupo/grupofornecedor.html")


def list_prestador(request):
    if request.method == 'POST':
        
        search = request.POST.get('nome_prestador')
        lista_prestador = PrestadorServico.objects.filter(prestadorname__contains=search)

        if search == "":
            search = request.POST.get('email_prestador')
            lista_prestador = PrestadorServico.objects.filter(email__contains=search)

            if search == "":
                search = request.POST.get('cpf/cnpj_prestador')
                lista_prestador = PrestadorServico.objects.filter(numero_fiscal=search)

                if search == "":
                    return render(request, "grupo/grupoprestador.html")

        return render(request, "grupo/grupoprestador.html", {'lista_prestador':lista_prestador})
    else:
        return render(request, "grupo/grupoprestador.html")


def list_material(request):
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
                        return render(request, "grupo/grupomaterial.html")

        return render(request, "grupo/grupomaterial.html", {'lista_material':lista_material})
    else:
        return render(request, "grupo/grupomaterial.html")


def list_produto(request):
    return render(request, "grupo/grupoproduto.html")


def list_servico(request):
    return render(request, "grupo/gruposervico.html")
