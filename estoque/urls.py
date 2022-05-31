from django.urls import path
from estoque.views import get_funcionarios, create_product, update_product

urlpatterns = [
    path('funcionarios/', get_funcionarios, name='get-funcionarios'),
    path('create-produto/', create_product, name='create-product'),
    path('update-produto/', update_product, name='update-product'),
]