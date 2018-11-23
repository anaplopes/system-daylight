import uuid
from django.db import models


TIPOMATERIAL_CHOICES = (('Botão', 'Botão'), ('Barbante', 'Barbante'), ('Fita', 'Fita'), ('Laço', 'Laço'),
                        ('Linha', 'Linha'), ('Pedrarias', 'Pedrarias'), ('Renda', 'Renda'),
                        ('Viés', 'Viés'), ('Zíper', 'Zíper'),)

SUBTIPO_CHOICES = (('Acrílico', 'Acrílico'), ('Algodão', 'Algodão'), ('Alumínio', 'Alumínio'), ('Bombê', 'Bombê'),
                   ('Couro', 'Couro'), ('Cetim', 'Cetim'), ('Ferro', 'Ferro'), ('Lã', 'Lã'), ('Madeira', 'Madeira'),
                   ('Metal', 'Metal'), ('Nylon', 'Nylon'), ('Poliéster', 'Poliéster'), ('Plástico', 'Plástico'),
                   ('Seda', 'Seda'), ('Strass', 'Strass'), ('Vidrilho', 'Vidrilho'), ('Viscose', 'Viscose'),)
                    


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
