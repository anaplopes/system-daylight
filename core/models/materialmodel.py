import uuid
from django.db import models


TIPOMATERIAL_CHOICES = (('Tecido', 'Tecido'), ('Linha', 'Linha'), ('Botão', 'Botão'), ('Ziper', 'Ziper'),)

CLASSIFICACAO_CHOICES = (('Algodão', 'Algodão'), ('Nylon', 'Nylon'), ('Acrilico', 'Acrilico'),)

COR_CHOICES = (('Branco', 'Branco'), ('Preto', 'Preto'), ('Azul', 'Azul'), ('Verde', 'Verde'), ('Vermelho', 'Vermelho'),
                ('Amarelo', 'Amarelo'), ('Rosa', 'Rosa'), ('Laranja', 'Laranja'), ('Marron', 'Marron'), ('Cinza', 'Cinza'),
                ('Vinho', 'Vinho'), ('Lilás', 'Lilás'), ('Bege', 'Bege'), ('Botão', 'Botão'), ('Bordô', 'Bordô'), ('Roxo', 'Roxo'),
                ('Prata', 'Prata'), ('Dourado', 'Dourado'), ('Pink', 'Pink'), ('Jeans', 'Jeans'),)

###################### MATERIAL

class Material(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField('Nome do Material', max_length=100, null=False, blank=False) # descrição do material
    tipo_mprima = models.CharField('Tipo de Material', choices=TIPOMATERIAL_CHOICES, max_length=50, null=False, blank=False)
    classificacao = models.CharField('Classificação do Material', choices=CLASSIFICACAO_CHOICES, max_length=50, null=False, blank=False)
    cor = models.CharField('Cor do Material', choices=COR_CHOICES, max_length=20)
    cod_mprima = models.CharField('Código do Material', max_length=50) # código do fabricante do material
    nome_fabricante = models.CharField('Nome do Fabricante', max_length=50) # fabricante do material

    class Meta:
        db_table = 'Material'

    def __str__(self):
        return '{} {} {} ( {} )'.format(self.tipo_mprima, self.classificacao, self.cor, self.nome_fabricante)
