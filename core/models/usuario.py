from django.db import models
from django.core import validators
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin


PERFIL_CHOICES = (('G', 'Gerente'), ('A', 'Assistente'), ('V', 'Vendedor'),)

###################### Criação e administração do usuário e superuser.
class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField('Nome', max_length=50, null=False, blank=False)
    email = models.EmailField('E-mail', max_length=100, unique=True, null=False, blank=False)
    cpf = models.CharField('CPF', max_length=11, unique=True, null=False, blank=False)
    dt_nascimento = models.DateField('Data de Nascimento', max_length=10, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=11)
    perfil = models.CharField('Perfil', choices=PERFIL_CHOICES, max_length=1, null=False, blank=False)
    status_user = models.BooleanField("Ativo", default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'email', 'password']

    objects = UserManager()

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return self.nome
