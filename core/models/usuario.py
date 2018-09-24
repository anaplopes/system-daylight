import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


PERFIL_CHOICES = (('G', 'Gerente'), ('A', 'Assistente'), ('V', 'Vendedor'),)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField('Nome', max_length=100, default='')
    cpf = models.CharField('CPF', max_length=11, unique=True, null=True)
    dt_nascimento = models.DateField('Data de Nascimento', max_length=10, null=True)
    telefone = models.CharField('Telefone', max_length=11, default='')
    perfil = models.CharField('Perfil', choices=PERFIL_CHOICES, max_length=1)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile = Profile.objects.create(user=instance)
            profile.save()
