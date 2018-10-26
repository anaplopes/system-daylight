import uuid
from django.db import models

STATUS_CHOICES = (('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado'),)
FORM_PGTO_CHOICES = (('Débito', 'Débito'), ('Crédito', 'Crédito'), ('Boleto', 'Boleto'), ('Transferência', 'Transferência'),)
PRAZO_PGTO_CHOICES = (('À vista', 'À vista'), ('1x', '1x'), ('2x', '2x'), ('3x', '3x'),)

###################### Compra

class Compra(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_compra = models.IntegerField('Numero da Compra', unique=True, null=True, blank=True)
    fornecedor = models.ForeignKey(to='Fornecedor', on_delete=models.CASCADE, null=False, blank=False)
    data_compra = models.DateField('Data de Compra', max_length=10, null=False)
    data_entrega = models.DateField('Data de Entrega', max_length=10, null=True)
    valor_total = models.DecimalField('Valor Total', max_digits=10, decimal_places=2, null=False, max_length=5000, blank=False)
    forma_pagamento = models.CharField('Forma de Pagamento', default='', choices=FORM_PGTO_CHOICES, max_length=15, null=True, blank=True)
    prazo_pagamento = models.CharField('Prazo de Pagamento', default='', choices=PRAZO_PGTO_CHOICES, max_length=20, null=True, blank=True)
    responsavel = models.CharField('Nome do Responsavel', max_length=50, null=True, blank=True)
    status = models.CharField('Status do Pedido', default='Em andamento', choices=STATUS_CHOICES, max_length=20, null=False, blank=False)
    observacao = models.TextField('Observação', max_length=1000, null=True, blank=True)

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
