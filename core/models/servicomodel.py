import uuid
from django.db import models


SERVICO_CHOICES = (('Costura', 'Costura'), ('Estampa', 'Estampa'), ('Bordado', 'Bordado'),)
TIPOSERVICO_CHOICES = (('Fabricação', 'Fabricação'), ('Reparo', 'Reparo'),)
STATUS_CHOICES = (('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado'),)

###################### SERVIÇO

class Servico(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_servico = models.IntegerField('Numero do Serviço', unique=True, null=True, blank=True)
    prestador = models.ForeignKey(to='PrestadorServico', on_delete=models.CASCADE, null=False, blank=False)
    data_servico = models.DateField('Data do Serviço', max_length=10, null=False)
    data_entrega = models.DateField('Data de Entrega', max_length=10, null=False)
    tipo_servico = models.CharField('Tipo de Serviço', choices=TIPOSERVICO_CHOICES, max_length=10, null=False, blank=False)
    servico = models.CharField('Serviço', choices=SERVICO_CHOICES, max_length=7, null=False, blank=False)
    status = models.CharField('Status do Pedido', default='Em andamento', choices=STATUS_CHOICES, max_length=20, null=False, blank=False)
    valor_total = models.DecimalField('Valor Total', max_digits=10, decimal_places=2, null=False, max_length=5000, blank=False)
    observacao = models.TextField('Observação', max_length=1000, null=True, blank=True)
    

    class Meta:
        db_table = 'Servico'
    


    def save(self, *args, **kwargs):
        if self._state.adding:
            last_servico = type(self).objects.all().aggregate(largest=models.Max('numero_servico'))['largest']
            if last_servico is None:
                self.numero_servico = 1
            else:
                self.numero_servico = last_servico + 1
        super(Servico, self).save(*args, **kwargs)
