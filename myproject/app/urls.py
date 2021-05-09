from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='list'),
    path('<slug:slug>/', views.ProdutoDetailView.as_view(), name='detail')
]