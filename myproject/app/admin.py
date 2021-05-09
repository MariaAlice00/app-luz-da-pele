from django.contrib import admin
from .models import *


#admin.site.register(Categoria)
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'descricao')
    prepopulated_fields = {'slug': ('nome',)}

#admin.site.register(Produto)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','slug', 'imagem', 'descricao', 'valor', 'categoria')
    prepopulated_fields = {'slug': ('nome',)}