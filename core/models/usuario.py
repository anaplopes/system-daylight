from django.db import models
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


PERFIL_CHOICES = (('G', 'Gerente'), ('A', 'Assistente'), ('V', 'Vendedor'),)

###################### Criação e administração do usuário e superuser.
class UsuarioManager(BaseUserManager):
    
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError(_('Email precisa ser preenchido'))
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    nome = models.CharField('Nome', max_length=50, null=False, blank=False)
    email = models.EmailField('E-mail', max_length=100, unique=True, null=False, blank=False)
    cpf = models.CharField('CPF', max_length=11, unique=True, null=False, blank=False)
    dt_nascimento = models.DateField('Data de Nascimento', max_length=10, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=11)
    perfil = models.CharField('Perfil', choices=PERFIL_CHOICES, max_length=1, null=False, blank=False)
    status_user = models.BooleanField("Ativo", default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UsuarioManager()

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return self.nome
