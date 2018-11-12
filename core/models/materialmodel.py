import uuid
from django.db import models


TIPOMATERIAL_CHOICES = (('Linha', 'Linha'), ('Botão', 'Botão'), ('Zíper', 'Zíper'),
                        ('Barbante', 'Barbante'), ('Fita', 'Fita'), ('Laço', 'Laço'), ('Barbante', 'Barbante'),
                        ('Viés', 'Viés'), ('Pedrarias', 'Pedrarias'), ('Renda', 'Renda'),)

SUBTIPO_CHOICES = (('Algodão', 'Algodão'), ('Couro', 'Couro'), ('Nylon', 'Nylon'), ('Acrilico', 'Acrilico'),
                        ('Alumínio', 'Alumínio'), ('Metal', 'Metal'), ('Plástico', 'Plástico'), ('Strass', 'Strass'),
                        ('Vidrilho', 'Vidrilho'),)


###################### MATERIAL

class Material(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField('Descrição do Material', max_length=100, null=False, blank=False) # descrição do material
    tipo_material = models.CharField('Tipo de Material', choices=TIPOMATERIAL_CHOICES, max_length=20, null=False, blank=False)
    Subtipo_material = models.CharField('Subtipo de Material', choices=SUBTIPO_CHOICES, max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'Material'

    def __str__(self):
        return '{} {}'.format(self.tipo_material, self.Subtipo_material)
