from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from painel.models import Product, Category

def index(request):
    # Obter todas as categorias (marcas) para exibir no index
    categories = Category.objects.all()
    return render(request, 'nucleo/index.html', {
        'page_name': 'index',
        'categories': categories
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