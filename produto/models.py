from django.db import models
from django.conf import settings
import os
from PIL import Image

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    image = models.ImageField(
        upload_to='produto_imagens/%Y/%m', blank=True, null=True
    )
    slug = models.SlugField(unique=True)
    preco = models.FloatField(default=0)
    preco_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variáveis'),
            ('S', 'Simples')
        )
    )


    def __str__(self):
        return self.nome
        