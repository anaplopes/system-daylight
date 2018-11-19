from django.contrib.auth import login, logout
from django.urls import path
from . import views

#ciclo do projeto
# request > urls> views > model > response

urlpatterns = [
    path('', views.index, name='home'),
    path('entrar/', views.login, name='login'),
    path('sair/', views.logout, {'next_page': '/account/login/'}, name='logout'),
    path('change-password/', views.password_change, name='password_change'),

    path('gerencial/cadastrarusuario/', views.create_usuario, name='create_usuario'),
    path('gerencial/gerenciarusuario/', views.list_usuario, name='list_usuario'),
    #path('gerencial/gerenciarusuario/<uuid>/', views.delete_usuario, name='delete_usuario'),
    path('gerencial/cadastrarusuario/<uuid>/', views.update_usuario, name='update_usuario'),
    

    path('comercial/cadastrarcliente/', views.create_cliente, name='create_cliente'),
    path('comercial/gerenciarcliente/', views.list_cliente, name='list_cliente'),
    #path('comercial/gerenciarcliente/<uuid>/', views.delete_cliente, name='delete_cliente'),
    path('comercial/cadastrarcliente/<uuid>/', views.update_cliente, name='update_cliente'),

    path('comercial/cadastrarfornecedor/', views.create_fornecedor, name='create_fornecedor'),
    path('comercial/gerenciarfornecedor/', views.list_fornecedor, name='list_fornecedor'),
    #path('comercial/gerenciarfornecedor/<uuid>/', views.delete_fornecedor, name='delete_fornecedor'),
    path('comercial/cadastrarfornecedor/<uuid>/', views.update_fornecedor, name='update_fornecedor'),

    path('producao/cadastrarprestador/', views.create_prestador, name='create_prestador'),
    path('producao/gerenciarprestador/', views.list_prestador, name='list_prestador'),
    #path('producao/gerenciarprestador/<uuid>/', views.delete_prestador, name='delete_prestador'),
    path('producao/cadastrarprestador/<uuid>/', views.update_prestador, name='update_prestador'),

    path('comercial/cadastrarmaterial/', views.create_material, name='create_material'),
    path('comercial/gerenciarmaterial/', views.list_material, name='list_material'),
    #path('comercial/gerenciarmaterial/<uuid>/', views.delete_material, name='delete_material'),
    path('comercial/cadastrarmaterial/<uuid>/', views.update_material, name='update_material'),

    path('comercial/cadastrartecido/', views.create_tecido, name='create_tecido'),
    path('comercial/gerenciartecido/', views.list_tecido, name='list_tecido'),
    #path('comercial/gerenciartecido/<uuid>/', views.delete_tecido, name='delete_tecido'),
    path('comercial/cadastrartecido/<uuid>/', views.update_tecido, name='update_tecido'),

    path('comercial/cadastrarproduto/', views.create_produto, name='create_produto'),
    path('comercial/gerenciarproduto/', views.list_produto, name='list_produto'),
    #path('comercial/gerenciarproduto/<uuid>/', views.delete_produto, name='delete_produto'),
    path('comercial/cadastrarproduto/<uuid>/', views.update_produto, name='update_produto'),

    path('comercial/registrarpedido/', views.register_pedido, name='register_pedido'),
    path('comercial/gerenciarpedido/', views.list_pedido, name='list_pedido'),
    path('comercial/registrarpedido/<uuid>/', views.update_pedido, name='update_pedido'),

    path('comercial/registrarcompra/', views.register_compra, name='register_compra'),
    path('comercial/gerenciarcompra/', views.list_compra, name='list_compra'),
    path('comercial/registrarcompra/<uuid>/', views.update_compra, name='update_compra'),

    path('producao/registrarservico/', views.register_servico, name='register_servico'),
    path('producao/gerenciarservico/', views.list_servico, name='list_servico'),
    path('producao/registrarservico/<uuid>/', views.update_servico, name='update_servico'),

    path('expedicao', views.expedicao, name='expedicao'),
    path('detalhes_pedido/<uuid>', views.detalhes_pedido, name='detalhes_pedido'),
]
