from django.urls import path
from core.views import *

#ciclo do projeto
# request > urls> views > model > response

urlpatterns = [
    path('', home),
    path('login/', login),
    path('grupoUsuario/', grupoUsuario),
    path('usuario/', usuario),
    path('grupoCliente/', grupoCliente),
    path('cliente/', cliente),
    path('grupoFornecedor/', grupoFornecedor),
    path('fornecedor/', fornecedor),
    path('grupoPrestador/', grupoPrestador),
    path('prestador/', prestador),
    path('grupoProduto/', grupoProduto),
    path('produto/', produto),
    path('grupoServico/', grupoServico),
    path('servico/', servico),
    path('grupoMaterial/', grupoMaterial),
    path('material/', material),
    path('unidadeMedida/', unidadeMedida),
]