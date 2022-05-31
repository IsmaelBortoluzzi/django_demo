from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from estoque.forms import ProdutoForm
from estoque.models import Funcionario, Produtos


def get_funcionarios(request):
    context = dict()

    arrois = request.GET.get('arrois', None)

    sql = """SELECT * FROM FUNCIONARIO"""
    funcionarios = Funcionario.objects.raw(sql)

    context['funcionarios'] = funcionarios

    return render(request, 'funcionarios.html', context)


def create_product(request):
    context = dict()

    if request.method == 'GET':
        context = {
            'form': ProdutoForm()
        }

        return render(request, 'create_product.html', context)

    elif request.method == 'POST':

        form = ProdutoForm(request.POST)
        new_product = Produtos()

        if form.is_valid():
            new_product.nome = form.data.dict().get('nome')
            new_product.preco = form.data.dict().get('preco')
            new_product.numero = form.data.dict().get('numero')

            new_product.save()

        return HttpResponseRedirect(reverse_lazy('create-product'))


def update_product(request, product_id):
    context = dict()

    if request.method == 'GET':
        context = {
            'form': ProdutoForm(Produtos.objects.get(id=product_id))
        }

        return render(request, 'create_product.html', context)

    elif request.method == 'POST':

        form = ProdutoForm(request.POST)
        new_product = Produtos()

        if form.is_valid():
            new_product.nome = form.data.dict().get('nome')
            new_product.preco = form.data.dict().get('preco')
            new_product.numero = form.data.dict().get('numero')

            new_product.save()

        return HttpResponseRedirect(reverse_lazy('create-product'))
