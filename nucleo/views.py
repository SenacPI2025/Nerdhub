from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.defaults import page_not_found, server_error
from painel.models import Product, Category
from django.db.models import Q
import random

def index(request):
    # Obter todas as categorias (marcas) para exibir no index
    categories = Category.objects.all()
    
    # Obter produtos aleatórios para exibir como "destaque"
    # Primeiro pegamos todos os produtos ativos
    produtos_ativos = Product.objects.filter(is_active=True)
    
    # Selecionamos 20 produtos aleatórios (ou todos se tiver menos de 20)
    if produtos_ativos.count() > 20:
        # Pegamos 20 IDs aleatórios
        ids_aleatorios = random.sample(list(produtos_ativos.values_list('id', flat=True)), 20)
        # Buscamos os produtos com esses IDs
        produtos_destaque = Product.objects.filter(id__in=ids_aleatorios)
    else:
        # Se tiver menos de 20 produtos, pegamos todos
        produtos_destaque = produtos_ativos
    
    return render(request, 'nucleo/index.html', {
        'page_name': 'index',
        'categories': categories,
        'produtos_destaque': produtos_destaque
    })

def ver_carrinho(request):
    return HttpResponse("Carrinho ainda não implementado.")

def sobre(request):
    return render(request, 'nucleo/sobre.html', {'page_name': 'sobre'})

def suporte(request):
    return render(request, 'nucleo/suporte.html', {'page_name': 'suporte'})

def produtos_por_marca(request, marca_slug):
    # Obter a categoria (marca) pelo slug
    category = get_object_or_404(Category, slug=marca_slug)
    
    # Obter todos os produtos dessa categoria
    produtos = Product.objects.filter(category=category, is_active=True)
    
    return render(request, 'nucleo/marca_produtos.html', {
        'marca': category,
        'produtos': produtos
    })

def detalhes_produto(request, produto_id):
    # Obter o produto pelo ID
    produto = get_object_or_404(Product, id=produto_id, is_active=True)
    
    return render(request, 'nucleo/detalhes_produto.html', {
        'produto': produto
    })

def custom_404(request, exception):
    """Manipulador de erro 404 personalizado"""
    return render(request, 'nucleo/404.html', status=404)

def custom_500(request):
    """Manipulador de erro 500 personalizado"""
    return render(request, 'nucleo/500.html', status=500)