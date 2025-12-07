#!/usr/bin/env python
"""
Script para criar dados de exemplo para o NerdHub.
Este script cria categorias (marcas) e produtos de exemplo para testar a aplicação.
"""

import os
import sys
import django

# Adiciona o diretório raiz do projeto ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nerdhub.settings')
django.setup()

from painel.models import Category, Product

def create_categories():
    """Cria as categorias (marcas) principais"""
    categories_data = [
        {'name': 'Disney', 'slug': 'disney'},
        {'name': 'Marvel', 'slug': 'marvel'},
        {'name': 'Star Wars', 'slug': 'star-wars'},
        {'name': 'PlayStation', 'slug': 'playstation'},
        {'name': 'Xbox', 'slug': 'xbox'},
    ]
    
    created_count = 0
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
        if created:
            print(f"Categoria '{category.name}' criada com sucesso!")
            created_count += 1
        else:
            print(f"Categoria '{category.name}' já existe.")
    
    print(f"{created_count} categorias criadas.")
    return created_count

def create_sample_products():
    """Cria produtos de exemplo para cada categoria"""
    # Obter categorias existentes
    try:
        disney = Category.objects.get(slug='disney')
        marvel = Category.objects.get(slug='marvel')
        star_wars = Category.objects.get(slug='star-wars')
        playstation = Category.objects.get(slug='playstation')
        xbox = Category.objects.get(slug='xbox')
    except Category.DoesNotExist:
        print("Erro: Algumas categorias não foram encontradas. Execute create_categories() primeiro.")
        return 0
    
    products_data = [
        # Produtos Disney
        {
            'name': 'Boneco Mickey Mouse',
            'price': 129.90,
            'description': 'Boneco colecionável do Mickey Mouse',
            'category': disney,
            'stock': 10,
            'brand': 'Disney',
            'model': 'Classic Mickey',
        },
        {
            'name': 'Caneca Disney Princess',
            'price': 49.90,
            'description': 'Caneca térmica com princesas da Disney',
            'category': disney,
            'stock': 25,
            'brand': 'Disney',
            'model': 'Princess Collection',
        },
        
        # Produtos Marvel
        {
            'name': 'Camiseta Avengers',
            'price': 89.90,
            'description': 'Camiseta oficial dos Vingadores',
            'category': marvel,
            'stock': 15,
            'brand': 'Marvel',
            'model': 'Avengers Logo',
        },
        {
            'name': 'Action Figure Spider-Man',
            'price': 199.90,
            'description': 'Action figure do Homem-Aranha com 15cm',
            'category': marvel,
            'stock': 8,
            'brand': 'Marvel',
            'model': 'Spider-Man Classic',
        },
        
        # Produtos Star Wars
        {
            'name': 'Lightsaber Replica',
            'price': 299.90,
            'description': 'Réplica da lightsaber do Luke Skywalker',
            'category': star_wars,
            'stock': 5,
            'brand': 'Star Wars',
            'model': 'Luke Skywalker Lightsaber',
        },
        
        # Produtos PlayStation
        {
            'name': 'Controle DualSense',
            'price': 299.90,
            'description': 'Controle oficial do PlayStation 5',
            'category': playstation,
            'stock': 20,
            'brand': 'Sony',
            'model': 'DualSense',
        },
        
        # Produtos Xbox
        {
            'name': 'Controle Xbox Series X',
            'price': 249.90,
            'description': 'Controle oficial do Xbox Series X|S',
            'category': xbox,
            'stock': 18,
            'brand': 'Microsoft',
            'model': 'Xbox Wireless Controller',
        },
    ]
    
    created_count = 0
    for prod_data in products_data:
        # Verificar se o produto já existe
        existing_product = Product.objects.filter(
            name=prod_data['name'],
            category=prod_data['category']
        ).first()
        
        if not existing_product:
            product = Product.objects.create(**prod_data)
            print(f"Produto '{product.name}' criado com sucesso!")
            created_count += 1
        else:
            print(f"Produto '{existing_product.name}' já existe.")
    
    print(f"{created_count} produtos criados.")
    return created_count

def main():
    """Função principal para executar a criação de dados"""
    print("=== Criando dados de exemplo para NerdHub ===")
    
    # Criar categorias
    print("\n1. Criando categorias...")
    create_categories()
    
    # Criar produtos
    print("\n2. Criando produtos...")
    create_sample_products()
    
    print("\n=== Processo concluído! ===")

if __name__ == '__main__':
    main()