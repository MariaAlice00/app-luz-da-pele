import json 
from .models import *


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart']) 
    except:
        cart = {}
        
    print('Cart:', cart)
    items = []
    pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = pedido['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]["quantidade"]

            produto = Produto.objects.get(id=i)
            total = (produto.valor * cart[i]["quantidade"])    

            pedido['get_cart_total'] += total  
            pedido['get_cart_items'] += cart[i]['quantidade']  

            item = {
                'produto':{
                    'id': produto.id,
                    'nome': produto.nome,
                    'valor':produto.valor,
                    'imagemURL':produto.imagemURL,
                },
                'quantidade':cart[i]["quantidade"],
                'get_total':total
            }
            items.append(item)
        except:
            pass
    
    return {'cartItems': cartItems, 'pedido': pedido, 'items': items}


def cartData(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, completo=False)
        items = pedido.pedidoitem_set.all()
        cartItems = pedido.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        pedido = cookieData['pedido']
        items = cookieData['items']

    return {'cartItems': cartItems, 'pedido': pedido, 'items': items}


def guestPedido(request, data):
    print('Usuário não está logado...')

    print('COOKIES:', request.COOKIES)
    nome = data['form']['nome']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']
    cliente, created = Cliente.objects.get_or_create(
        email=email,
    )
    cliente.nome = nome
    cliente.save()

    pedido = Pedido.objects.create(
        cliente=cliente,
        completo=False,
    )

    for item in items:
        produto = Produto.objects.get(id=item['produto']['id'])

        pedidoItem = PedidoItem.objects.create(
            produto=produto,
            pedido=pedido, 
            quantidade=item['quantidade'],
        )

    return cliente, pedido