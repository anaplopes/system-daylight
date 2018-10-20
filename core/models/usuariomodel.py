import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


PERFIL_CHOICES = (('G', 'Gerente'), ('A', 'Assistente'), ('V', 'Vendedor'),)

class CustomUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField('Nome', max_length=100, null=True)
    cpf = models.CharField('CPF', max_length=11, unique=True, null=True)
    dt_nascimento = models.DateField('Data de Nascimento', max_length=10, null=True)
    telefone = models.CharField('Telefone', max_length=11, null=True)
    perfil = models.CharField('Perfil', choices=PERFIL_CHOICES, max_length=1, default='A')
