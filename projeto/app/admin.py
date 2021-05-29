from django.contrib import admin
from .models import Produto, Venda, Cliente


admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Cliente)