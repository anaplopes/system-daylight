import uuid
from django.db import models


TIPOTECIDO_CHOICES = (('Algodão', 'Algodão'), ('Tricoline', 'Tricoline'), ('Oxford', 'Oxford'), ('Linho', 'Linho'),
                        ('Brim', 'Brim'), ('Cetim', 'Cetim'), ('Moleton', 'Moleton'), ('Jeans', 'Jeans'),
                        ('Couro', 'Couro'), ('Malha', 'Malha'),)


###################### TECIDO

class Tecido(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tecido = models.CharField('Tecido', max_length=100, null=False, blank=False) # descrição do material
    tipo_tecido = models.CharField('Tipo de Tecido', choices=TIPOTECIDO_CHOICES, max_length=50, null=True, blank=True)
    nome_fabricante = models.CharField('Nome do Fabricante', max_length=50, null=True, blank=True) # fabricante do material

    class Meta:
        db_table = 'Tecido'

    def __str__(self):
        return '{} ( {} )'.format(self.tipo_tecido, self.nome_fabricante)
