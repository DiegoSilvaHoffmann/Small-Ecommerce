from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

import re

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=60)
    numero = models.CharField(max_length=5)
    completo = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=15,
        default='CAT',
        choices=(
            ('CAT', 'Catalunha' ),
            ('RS', 'Rio Grande do Sul'),
            ('SC', 'Santa Catarina'),
            ('SP', 'Sao Paulo'),
            ('VE', 'Veneto'),
        )
    )

    def __str__(self):
        return f'{self.usuario}'
    
    def clean(self):
        error_messages = {}

        if re.search(r'[^0-9]', self.cep):
            error_messages['cep'] = 'Digite um codigo postal valido'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'