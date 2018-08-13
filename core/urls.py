from django.urls import path
from . import views

#ciclo do projeto
# request > urls> views > model > response

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='entrar'),

    path('cadastro/usuario/', views.create_usuario, name='create_usuario'),
    path('grupo/grupousuario/', views.list_usuario, name='list_usuario'),
    path('grupo/grupousuario/<id>/', views.delete_usuario, name='delete_usuario'),
    path('cadastro/usuario/<id>/', views.update_usuario, name='update_usuario'),
    
    path('cadastro/cliente/', views.create_cliente, name='create_cliente'),
    path('grupo/grupocliente/', views.list_cliente, name='list_cliente'),
    path('grupo/grupocliente/<id>/', views.delete_cliente, name='delete_cliente'),
    path('cadastro/cliente/<id>/', views.update_cliente, name='update_cliente'),
    
    path('cadastro/fornecedor/', views.create_fornecedor, name='create_fornecedor'),
    path('grupo/grupofornecedor/', views.list_fornecedor, name='list_fornecedor'),
    path('grupo/grupofornecedor/<id>/', views.delete_fornecedor, name='delete_fornecedor'),
    path('cadastro/fornecedor/<id>/', views.update_fornecedor, name='update_fornecedor'),
    
    path('cadastro/prestador/', views.create_prestador, name='create_prestador'),
    path('grupo/grupoprestador/', views.list_prestador, name='list_prestador'),
    path('grupo/grupoprestador/<id>/', views.delete_prestador, name='delete_prestador'),
    path('cadastro/prestador/<id>/', views.update_prestador, name='update_prestador'),
    
    path('cadastro/material/', views.create_material, name='create_material'),
    path('grupo/grupomaterial/', views.list_material, name='list_material'),
    path('grupo/grupomaterial/<id>/', views.delete_material, name='delete_material'),
    path('cadastro/material/<id>/', views.update_material, name='update_material'),
    
    path('cadastro/unidademedida/', views.create_medida, name='create_medida'),
    
    path('cadastro/produto/', views.create_produto, name='create_produto'),
    path('grupo/grupoproduto/', views.list_produto, name='list_produto'),
    path('grupo/grupoproduto/<id>/', views.delete_produto, name='delete_produto'),
    path('cadastro/produto/<id>/', views.update_produto, name='update_produto'),
    
    path('cadastro/servico/', views.create_servico, name='create_servico'),
    path('grupo/gruposervico/', views.list_servico, name='list_servico'),
    path('grupo/gruposervico/<id>/', views.delete_servico, name='delete_servico'),
    path('cadastro/servico/<id>/', views.update_servico, name='update_servico'),

]
