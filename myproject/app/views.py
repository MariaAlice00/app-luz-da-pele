from django.views.generic import DetailView, ListView
from .models import *


class ProdutoListView(ListView):
    model = Produto


class ProdutoDetailView(DetailView):
    model = Produto