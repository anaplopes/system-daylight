from django.db import models


MODELOPRODUTO_CHOICES = (('Ux', 'Unissex'), ('F', 'Feminino'), ('M', 'Masculino'),)
TAMANHOPRODUTO_CHOICES = (('Único', 'Único'), ('PP', 'PP'), ('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG'), ('2G', '2G'), ('3G', '3G'), ('4G', '4G'), ('XG', 'XG'), ('EXG', 'EXG'),)

###################### PRODUTO

class Produto(models.Model):
    tipo_produto = models.CharField('Tipo de Produto', max_length=50, null=False, blank=False) # camiseta, avental, calça e etc.
    produto = models.CharField('Nome do Produto', max_length=100, null=False, blank=False) # descrição do produto
    modelo = models.CharField('Modelo do produto', choices=MODELOPRODUTO_CHOICES, max_length=2, null=False, blank=False) # Masculino, Feminina e etc.
    classificacao = models.CharField('Classificação do Produto', max_length=50, null=False, blank=False) # restaurante, gastronomia, confeitaria, buffet e etc.
    tamanho = models.CharField('Tamanho do Produto', choices=TAMANHOPRODUTO_CHOICES, max_length=5, null=False, blank=False)  # P, M, G e etc.
    cor = models.CharField('Cor do Produto', max_length=50, null=False, blank=False)
    valor_venda = models.DecimalField('Valor do Produto', max_digits=10, decimal_places=2, null=False, blank=False)
    especificacao = models.TextField('Especificação do Produto', max_length=1000, null=False, blank=False)

    class Meta:
        db_table = 'Produto'
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(self.tipo_produto, self.classificacao, self.produto, self.modelo, self.tamanho, self.cor)