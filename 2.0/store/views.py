from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    
    produtos = Produto.objects.all()
    context = {'produtos': produtos, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    pedido = data['pedido']
    items = data['items']

    context = {'items': items, 'pedido': pedido, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    pedido = data['pedido']
    items = data['items']

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
    transacao_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        total = float(data['form']['total'])
        pedido.transacao_id = transacao_id

        if total == float(pedido.get_cart_total):
            pedido.completo = True
        pedido.save()

    else:
        print('Usuário não está logado...')

    return JsonResponse('Pagamento completo!', safe=False)
