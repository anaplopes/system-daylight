import uuid
from django.db import models


###################### MATERIAL

class Material(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField('Nome do Material', max_length=100, null=False, blank=False) # descrição do material
    tipo_mprima = models.CharField('Tipo de Material', max_length=50, null=False, blank=False) # tecido, linha, botão, ziper e etc.
    classificacao = models.CharField('Classificação do Material', max_length=50, null=False, blank=False) # algodão, nylon, acrilico e etc.
    cor = models.CharField('Cor do Material', max_length=50)
    cod_mprima = models.CharField('Código do Material', max_length=50) # código do fabricante do material
    nome_fabricante = models.CharField('Nome do Fabricante', max_length=50) # fabricante do material

    class Meta:
        db_table = 'Material'

    def __str__(self):
        return '{} {} {} ( {} )'.format(self.tipo_mprima, self.classificacao, self.cor, self.nome_fabricante)
