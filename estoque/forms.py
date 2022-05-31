from django import forms
from estoque.models import Produtos


class ProdutoForm(forms.Form):
    nome = forms.CharField(max_length=255, label='Nome', required=True)
    numero = forms.IntegerField(label='GTIN', required=True)
    preco = forms.FloatField(label='Preço', required=True)

