import uuid
from django.db import models


COR_CHOICES = (('Branco', 'Branco'), ('Preto', 'Preto'), ('Azul', 'Azul'), ('Verde', 'Verde'), ('Vermelho', 'Vermelho'),
                ('Amarelo', 'Amarelo'), ('Rosa', 'Rosa'), ('Laranja', 'Laranja'), ('Marron', 'Marron'), ('Cinza', 'Cinza'),
                ('Vinho', 'Vinho'), ('Lilás', 'Lilás'), ('Bege', 'Bege'), ('Botão', 'Botão'), ('Bordô', 'Bordô'), ('Roxo', 'Roxo'),
                ('Prata', 'Prata'), ('Dourado', 'Dourado'), ('Pink', 'Pink'), ('Jeans', 'Jeans'),)

STATUS_CHOICES = (('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado'),)

FORM_PGTO_CHOICES = (('À vista', 'À vista'), ('1x', '1x'), ('2x', '2x'), ('3x', '3x'),)

###################### PEDIDO

class Pedido(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_pedido = models.IntegerField('Numero do Pedido', unique=True, null=False, blank=False)
    cliente = models.ForeignKey(to='Cliente', on_delete=models.CASCADE, null=False, blank=False)
    data_compra = models.DateField('Data de Compra', max_length=10, null=False)
    data_entrega = models.DateField('Data de Entrega', max_length=10, null=False)
    valor_total = models.DecimalField('Valor Total', max_digits=10, decimal_places=2, null=False, max_length=5000, blank=False)
    forma_pagamento = models.CharField('Forma de Pagamento', default='', choices=FORM_PGTO_CHOICES, max_length=15, null=True, blank=True)
    endereco_entrega = models.CharField('Endereço Entrega', max_length=100, null=True, blank=True)
    solicitante = models.CharField('Nome do Solicitante', max_length=50, null=True, blank=True)
    status = models.CharField('Status do Pedido', default='Em andamento', choices=STATUS_CHOICES, max_length=20, null=False, blank=False)

    class Meta:
        db_table = 'Pedido'
