from .index import index
from .login import login, logout
from .usuarioview import create_usuario, update_usuario, delete_usuario, list_usuario
from .clienteview import create_cliente, update_cliente, delete_cliente, list_cliente
from .fornecedorview import create_fornecedor, update_fornecedor, delete_fornecedor, list_fornecedor
from .prestadorview import create_prestador, update_prestador, delete_prestador, list_prestador
from .materialview import create_material, update_material, delete_material, list_material
from .tecidoview import create_tecido, update_tecido, delete_tecido, list_tecido
from .produtoview import create_produto, update_produto, delete_produto, list_produto
from .servicoview import create_servico, update_servico, delete_servico, list_servico
from .compraview import register_compra, list_compra
from .pedidoview import register_pedido, update_pedido, list_pedido


