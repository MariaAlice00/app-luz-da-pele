from django.shortcuts import render
from .models import *


def store(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        items = pedido.pedidoitem_set.all()
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'pedido': pedido}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        items = pedido.pedidoitem_set.all()
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'pedido': pedido}
    return render(request, 'store/checkout.html', context)