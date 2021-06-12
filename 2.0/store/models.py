from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Usuário")
    nome = models.CharField(max_length=200, verbose_name="Nome")
    email = models.CharField(max_length=200, verbose_name="Email")

    def __str__(self):
        return self.nome


class Produto(models.Model):
    CATEGORY_CHOICES = [
        ('facial', 'Facial'),
        ('corpo', 'Corpo'),
        ('cabelos', 'Cabelos'),
    ]
    nome = models.CharField(max_length=200, verbose_name="Nome")
    categoria = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name="Categoria")
    marca = models.CharField(max_length=200, verbose_name="Marca")
    base = models.CharField(max_length=200, verbose_name="Base")
    valor = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Valor")
    caracteristicas = models.TextField(verbose_name="Características")
    indicacao = models.TextField(verbose_name="Indicação")
    utilidade = models.TextField(verbose_name="Utilidade")
    ingredientes = models.TextField(verbose_name="Ingredientes")
    mododeuso = models.TextField(verbose_name="Modo de Uso")
    precaucoes = models.TextField(verbose_name="Precauções")
    imagem = models.ImageField(null=True, blank=True, verbose_name="Imagem")

    def __str__(self):
        return self.nome

    @property
    def imagemURL(self):
        try:
            url = self.imagem.url
        except:
            url = ''
        return url


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Cliente")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data do Pedido")
    completo = models.BooleanField(default=False, null=True, blank=False, verbose_name="Completo")
    id_transacao = models.CharField(max_length=200, null=True, verbose_name="ID da transação")

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        pedidoitens = self.pedidoitem_set.all()
        total = sum([item.get_total for item in pedidoitens])
        return total

    @property
    def get_cart_items(self):
        pedidoitens = self.pedidoitem_set.all()
        total = sum([item.quantidade for item in pedidoitens])
        return total    


class PedidoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Produto")
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Pedido")
    quantidade = models.IntegerField(default=0, null=True, blank=True, verbose_name="Quantidade")
    data_add = models.DateTimeField(auto_now_add=True, verbose_name="Data da Adição")

    @property
    def get_total(self):
        total = self.produto.valor * self.quantidade
        return total

    @property
    def get_quantidade(self):
        quant = self.quantidade
        return quant

