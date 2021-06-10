from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('app/<int:pk>/', views.detalhes_produto, name='detalhes_produto'),
    path('app/novo/', views.novo_produto, name='novo_produto'),
    path('app/<int:pk>/editar/', views.editar_produto, name='editar_produto'),
    path('app/<pk>/remover/', views.remover_produto, name='remover_produto'),
]
