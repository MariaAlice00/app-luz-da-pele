from django.db import models
from django.conf import settings
from django.utils import timezone


class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ('facial', 'Facial'),
        ('corpo', 'Corpo'),
        ('cabelos', 'Cabelos'),
    ]
    nome = models.CharField(max_length=200, verbose_name="Nome")
    categoria = models.CharField(max_length=100, choices=CATEGORIA_CHOICES, verbose_name="Categoria")
    marca = models.CharField(max_length=200, verbose_name="Marca")
    base = models.CharField(max_length=200, verbose_name="Base")
    valor = models.FloatField(verbose_name="Valor")
    caracteristicas = models.TextField(verbose_name="Características")
    indicacao = models.TextField(verbose_name="Indicação")
    utilidade = models.TextField(verbose_name="Utilidade")
    ingredientes = models.TextField(verbose_name="Ingredientes")
    mododeuso = models.TextField(verbose_name="Modo de Uso")
    precaucoes = models.TextField(verbose_name="Precauções")

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Venda(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='pedidos')
    valor = models.FloatField()
    data = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return 'venda efetuada'
