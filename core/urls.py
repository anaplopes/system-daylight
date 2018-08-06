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

]