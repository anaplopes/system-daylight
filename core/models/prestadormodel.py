import uuid
from django.db import models


FISCAL_CHOICES = (('PF', 'Pessoal Física'), ('PJ', 'Pessoa Jurídica'),)

###################### PRESTADOR

class PrestadorServico(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_fiscal = models.CharField('Classificação fiscal', choices=FISCAL_CHOICES, max_length=2, null=False, blank=False)
    prestadorname = models.CharField('Prestador de Serviço', max_length=200, null=False, blank=False)
    email = models.EmailField('E-mail', max_length=100, unique=True, null=False, blank=False)
    numero_fiscal = models.CharField('CNPJ/CPF', max_length=18, unique=True, null=False, blank=False)
    endereco = models.CharField('Endereço', max_length=200)
    bairro = models.CharField('Bairro', max_length=200)
    cidade = models.CharField('Cidade', max_length=200)
    cep = models.CharField('CEP', max_length=9)
    uf = models.CharField('UF', max_length=2)
    telefone = models.CharField('Telefone', max_length=14)


    class Meta:
        db_table = 'Prestador'
