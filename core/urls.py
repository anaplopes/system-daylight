from django.urls import path
from core.views import *

#ciclo do projeto
# request > urls> views > model > response

urlpatterns = [
    path('', home),
    path('login/', login),

    path('cadastro/usuario/', create_usuario, name='create_usuario'),
    path('grupo/grupoUsuario/', list_usuario, name='list_usuario'),
    path('grupo/grupoUsuario/<id>/', delete_usuario, name='delete_usuario'),
    path('cadastro/usuario/<id>/', update_usuario, name='update_usuario'),
    
    path('cadastro/cliente/', create_cliente, name='create_cliente'),
    path('grupo/grupoCliente/', list_cliente, name='list_cliente'),
    path('grupo/grupoCliente/<id>/', delete_cliente, name='delete_cliente'),
    path('cadastro/cliente/<id>/', update_cliente, name='update_cliente'),
    
    path('cadastro/fornecedor/', create_fornecedor, name='create_fornecedor'),
    path('grupo/grupoFornecedor/', list_fornecedor, name='list_fornecedor'),
    path('grupo/grupoFornecedor/<id>/', delete_fornecedor, name='delete_fornecedor'),
    path('cadastro/fornecedor/<id>/', update_fornecedor, name='update_fornecedor'),
    
    path('cadastro/prestador/', create_prestador, name='create_prestador'),
    path('grupo/grupoPrestador/', list_prestador, name='list_prestador'),
    path('grupo/grupoPrestador/<id>/', delete_prestador, name='delete_prestador'),
    path('cadastro/prestador/<id>/', update_prestador, name='update_prestador'),
    
    path('cadastro/material/', create_material, name='create_material'),
    path('grupo/grupoMaterial/', list_material, name='list_material'),
    path('grupo/grupoMaterial/<id>/', delete_material, name='delete_material'),
    path('cadastro/material/<id>/', update_material, name='update_material'),
    
    path('cadastro/unidadeMedida/', create_medida, name='create_medida'),
    
    path('cadastro/produto/', create_produto, name='create_produto'),
    path('grupo/grupoProduto/', list_produto, name='list_produto'),
    path('grupo/grupoProduto/<id>/', delete_produto, name='delete_produto'),
    path('cadastro/produto/<id>/', update_produto, name='update_produto'),
    
    path('cadastro/servico/', create_servico, name='create_servico'),
    path('grupo/grupoServico/', list_servico, name='list_servico'),
    path('grupo/grupoServico/<id>/', delete_servico, name='delete_servico'),
    path('cadastro/servico/<id>/', update_servico, name='update_servico'),

]
