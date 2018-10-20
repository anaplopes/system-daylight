import uuid
from django.db import models


MODELOPRODUTO_CHOICES = (('Unissex', 'Unissex'), ('Feminino', 'Feminino'), ('Masculino', 'Masculino'),)

TAMANHOPRODUTO_CHOICES = (('Único', 'Único'), ('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG'), ('2G', '2G'),
                            ('3G', '3G'), ('4G', '4G'), ('XG', 'XG'), ('EXG', 'EXG'),)

TIPOPRODUTO_CHOICES = (('Calça', 'Calça'), ('Camiseta', 'Camiseta'), ('Camisa Polo', 'Camisa Polo'), ('Dolma', 'Dolma'), ('Jaleco', 'Jaleco'), ('Avental', 'Avental'),
                        ('Toca', 'Toca'), ('Macacão', 'Macacão'), ('Jardineira', 'Jardineira'), ('Conjunto', 'Conjunto'), ('Uniforme', 'Uniforme'),
                        ('Meio Avental', 'Meio Avental'), ('Camisa Social', 'Camisa Social'),)

CLASSIFICACAO_CHOICES = (('Camuflada', 'Camuflada'), ('Baby Look', 'Baby Look'), ('Tradicional', 'Tradicional'), ('Chefe Ronaldo Zara', 'Chefe Ronaldo Zara'),
                            ('Esmalteria', 'Esmalteria'), ('Restaurante', 'Restaurante'), ('Confeitaria', 'Confeitaria'), ('Garçom', 'Garçom'),
                            ('Chefe', 'Chefe'), ('Padaria', 'Padaria'), ('Kimono Sushiman', 'Kimono Sushiman'), ('Atendente', 'Atendente'), ('Japones', 'Japones'),
                            ('Recepcionista', 'Recepcionista'), ('Aux. Cozinha', 'Aux. Cozinha'), ('Aux. Limpeza', 'Aux. Limpeza'), ('Cozinheiro', 'Cozinheiro'),)


###################### PRODUTO

class Produto(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_produto = models.CharField('Tipo de Produto', choices=TIPOPRODUTO_CHOICES, max_length=50, null=False, blank=False)
    produto = models.CharField('Nome do Produto', max_length=100, null=False, blank=False) # descrição do produto
    modelo = models.CharField('Modelo do produto', choices=MODELOPRODUTO_CHOICES, max_length=10, null=False, blank=False)
    classificacao = models.CharField('Classificação do Produto', choices=CLASSIFICACAO_CHOICES, max_length=50, null=False, blank=False)
    tamanho = models.CharField('Tamanho do Produto', choices=TAMANHOPRODUTO_CHOICES, max_length=5, null=False, blank=False)    

    class Meta:
        db_table = 'Produto'
    
    def __str__(self):
        return '{} {} {} ( {} )'.format(self.tipo_produto, self.classificacao, self.tamanho, self.modelo)