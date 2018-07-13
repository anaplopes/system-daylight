from django.db import models


SERVICO_CHOICES = (('Costura', 'Costura'), ('Estampa', 'Estampa'), ('Bordado', 'Bordado'),)
TIPOSERVICO_CHOICES = (('Fabricação', 'Fabricação'), ('Reparo', 'Reparo'),)

###################### SERVIÇO

class Servico(models.Model):
    tipo_servico = models.CharField('Tipo de Serviço', choices=TIPOSERVICO_CHOICES, max_length=10, null=False, blank=False)
    servico = models.CharField('Serviço', choices=SERVICO_CHOICES, max_length=7, null=False, blank=False)
    tipo_produto = models.ForeignKey(to='Produto', on_delete=models.CASCADE, null=False, blank=False)
    valor_peca = models.DecimalField('Valor do Peça', max_digits=10, decimal_places=2, null=False, blank=False)

    class Meta:
        db_table = 'Servico'