from django.urls import path
from core.views import *

#ciclo do projeto
# request > urls> views > model > response

urlpatterns = [
    path('', home),
    path('login/', login),
    path('grupo/grupoUsuario/', grupoUsuario),
    path('cadastro/usuario/', usuario),
    path('grupo/grupoCliente/', grupoCliente),
    path('cadastro/cliente/', cliente),
    path('grupo/grupoFornecedor/', grupoFornecedor),
    path('cadastro/fornecedor/', fornecedor),
    path('grupo/grupoPrestador/', grupoPrestador),
    path('cadastro/prestador/', prestador),
    path('grupo/grupoProduto/', grupoProduto),
    path('cadastro/produto/', produto),
    path('grupo/grupoServico/', grupoServico),
    path('cadastro/servico/', servico),
    path('grupo/grupoMaterial/', grupoMaterial),
    path('cadastro/material/', material),
    path('cadastro/unidadeMedida/', unidadeMedida),
]