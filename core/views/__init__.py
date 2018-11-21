from .index import index
from .login import login, logout, check_gerente, check_vendedor, check_assistente
from .usuarioview import create_usuario, update_usuario, list_usuario, password_change
from .clienteview import create_cliente, update_cliente, list_cliente
from .fornecedorview import create_fornecedor, update_fornecedor, list_fornecedor
from .prestadorview import create_prestador, update_prestador, list_prestador
from .materialview import create_material, update_material, list_material
from .tecidoview import create_tecido, update_tecido, list_tecido
from .produtoview import create_produto, update_produto, list_produto
from .compraview import register_compra, update_compra, list_compra, detalhes_compra
from .pedidoview import register_pedido, update_pedido, list_pedido, detalhes_pedido
from .servicoview import register_servico, update_servico, list_servico, detalhes_servico
from .expedicaoview import expedicao
