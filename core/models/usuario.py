import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.db.models.signals import post_save
from django.dispatch import receiver



PERFIL_CHOICES = (('G', 'Gerente'), ('A', 'Assistente'), ('V', 'Vendedor'),)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True, null=False, blank=False)
    dt_nascimento = models.DateField('Data de Nascimento', max_length=10, null=True)
    telefone = models.CharField('Telefone', max_length=11)
    perfil = models.CharField('Perfil', choices=PERFIL_CHOICES, max_length=1, blank=False)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
