from django.db import models


###################### UNIDADE DE MEDIDA

class UnidadeMedida(models.Model):
    tecido = models.ForeignKey(to='Material', on_delete=models.CASCADE, null=False, blank=False)
    produto = models.ForeignKey(to='Produto', on_delete=models.CASCADE, null=False, blank=False)
    qtd_unidade = models.FloatField('Quantidade por unidade', null=False, blank=False)

    class Meta:
        db_table = 'Medida'
