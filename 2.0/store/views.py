from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *


def store(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        items = pedido.pedidoitem_set.all()
        cartItems = pedido.get_cart_items
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0, 'vazio': False}
        cartItems = pedido['get_cart_items']

    produtos = Produto.objects.all()
    context = {'produtos': produtos, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        items = pedido.pedidoitem_set.all()
        cartItems = pedido.get_cart_items
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0, 'vazio': False}
        cartItems = pedido['get_cart_items']

    context = {'items': items, 'pedido': pedido, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        items = pedido.pedidoitem_set.all()
        cartItems = pedido.get_cart_items
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0, 'vazio': False}
        cartItems = pedido['get_cart_items']

    context = {'items': items, 'pedido': pedido, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    cliente = request.user.cliente
    produto = Produto.objects.get(id=productId)
    pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)

    pedidoItem, created = PedidoItem.objects.get_or_create(pedido=pedido, produto=produto)

    if action == 'add':
        pedidoItem.quantidade = (pedidoItem.quantidade + 1)
    elif action == 'remove':
        pedidoItem.quantidade = (pedidoItem.quantidade - 1)
    pedidoItem.save()

    if pedidoItem.quantidade <= 0:
        pedidoItem.delete()

    return JsonResponse('Item foi adicionado', safe=False)


def processPedido(request):
    return JsonResponse('Pagamento completo!', safe=False)
