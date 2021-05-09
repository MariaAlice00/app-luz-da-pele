#from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



class Categoria(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True)
    descricao = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome



class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=255, unique=True)
    imagem = models.ImageField(upload_to='images')
    descricao = models.CharField(max_length=200, null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    categoria = models.ForeignKey('Categoria', related_name='itens', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'slug': self.slug})