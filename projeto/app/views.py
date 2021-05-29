from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Produto, Cliente, Venda
from .forms import ProdutoForm


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'app/listar_produtos.html', {'produtos': produtos})


def detalhes_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'app/detalhes_produto.html', {'produto': produto})


def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('detalhes_produto', pk=produto.pk)
    else:
        form = ProdutoForm()
    return render(request, 'app/editar_produto.html', {'form': form})


def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('detalhes_produto', pk=produto.pk)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'app/editar_produto.html', {'form': form})
