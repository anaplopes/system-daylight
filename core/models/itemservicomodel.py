import uuid
from django.db import models


COR_CHOICES = (('Branco', 'Branco'), ('Preto', 'Preto'), ('Azul', 'Azul'), ('Verde', 'Verde'), ('Vermelho', 'Vermelho'),
                ('Amarelo', 'Amarelo'), ('Rosa', 'Rosa'), ('Laranja', 'Laranja'), ('Marron', 'Marron'), ('Cinza', 'Cinza'),
                ('Vinho', 'Vinho'), ('Lilás', 'Lilás'), ('Bege', 'Bege'), ('Bordô', 'Bordô'), ('Roxo', 'Roxo'),
                ('Prata', 'Prata'), ('Dourado', 'Dourado'), ('Pink', 'Pink'), ('Jeans', 'Jeans'),)


###################### ITEM SERVIÇO

class ItemServico(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_servico = models.ForeignKey(to='Servico', on_delete=models.CASCADE, null=False, blank=False)
    produto = models.ForeignKey(to='Produto', on_delete=models.CASCADE, null=False, blank=False)
    cor = models.CharField('Cor', choices=COR_CHOICES, max_length=30, null=False, blank=False)
    quantidade = models.IntegerField('Quantidade', null=False, blank=False)
    valor_unitario = models.DecimalField('Valor Unitário', max_digits=10, decimal_places=2, null=False, blank=False)
    valor_total = models.DecimalField('Valor Total', max_digits=10, decimal_places=2, null=False, max_length=5000, blank=False)

    class Meta:
        db_table = 'ItemServico'
