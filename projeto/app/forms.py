from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('categoria', 'nome', 'marca', 'base', 'caracteristicas', 'valor', 'indicacao', 'utilidade', 'ingredientes', 'mododeuso', 'precaucoes',)

