import uuid
from django.db import models

STATUS_CHOICES = (('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado'),)
FORM_PGTO_CHOICES = (('Débito', 'Débito'), ('Crédito', 'Crédito'), ('Boleto', 'Boleto'), ('Transferência', 'Transferência'),)
PRAZO_PGTO_CHOICES = (('À vista', 'À vista'), ('1x', '1x'), ('2x', '2x'), ('3x', '3x'),)
COR_CHOICES = (('Branco', 'Branco'), ('Preto', 'Preto'), ('Azul', 'Azul'), ('Verde', 'Verde'), ('Vermelho', 'Vermelho'),
                ('Amarelo', 'Amarelo'), ('Rosa', 'Rosa'), ('Laranja', 'Laranja'), ('Marron', 'Marron'), ('Cinza', 'Cinza'),
                ('Vinho', 'Vinho'), ('Lilás', 'Lilás'), ('Bege', 'Bege'), ('Bordô', 'Bordô'), ('Roxo', 'Roxo'),
                ('Prata', 'Prata'), ('Dourado', 'Dourado'), ('Pink', 'Pink'), ('Jeans', 'Jeans'),)

###################### Compra

class Compra(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_compra = models.IntegerField('Numero da Compra', unique=True, null=True, blank=True)
    fornecedor = models.ForeignKey(to='Fornecedor', on_delete=models.CASCADE, null=False, blank=False)
    data_compra = models.DateField('Data de Compra', max_length=10, null=False)
    valor_total = models.DecimalField('Valor Total', max_digits=10, decimal_places=2, null=False, max_length=5000, blank=False)
    forma_pagamento = models.CharField('Forma de Pagamento', default='', choices=FORM_PGTO_CHOICES, max_length=15, null=True, blank=True)
    prazo_pagamento = models.CharField('Prazo de Pagamento', default='', choices=PRAZO_PGTO_CHOICES, max_length=20, null=True, blank=True)
    responsavel = models.CharField('Nome do Responsavel', max_length=50, null=True, blank=True)
    status = models.CharField('Status do Pedido', default='Em andamento', choices=STATUS_CHOICES, max_length=20, null=False, blank=False)
    observacao = models.TextField('Observação', max_length=1000, null=True, blank=True)
    numero_pedido = models.ForeignKey(to='Pedido', on_delete=models.CASCADE, null=False, blank=False)
    tecido = models.ForeignKey(to='Tecido', on_delete=models.CASCADE, null=False, blank=False)
    qtd_tecido = models.IntegerField('Quantidade Tecido', null=False, blank=False)
    valor_tecido = models.DecimalField('Valor Tecido', max_digits=10, decimal_places=2, null=False, max_length=5000, blank=False)
    cor_tecido = models.CharField('Cor Tecido', choices=COR_CHOICES, max_length=30, null=False, blank=False)


    class Meta:
        db_table = 'Compra'



    def save(self, *args, **kwargs):
        if self._state.adding:
            last_compra = type(self).objects.all().aggregate(largest=models.Max('numero_compra'))['largest']
            if last_compra is None:
                self.numero_compra = 1
            else:
                self.numero_compra = last_compra + 1
        super(Compra, self).save(*args, **kwargs)
