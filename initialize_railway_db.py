#!/usr/bin/env python
"""
Script para inicializar o banco de dados do Railway.
Este script cria as categorias (marcas) principais no banco de dados do Railway.
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

def initialize_categories():
    """Inicializa as categorias (marcas) principais no Railway"""
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

def main():
    """Função principal para executar a inicialização"""
    print("=== Inicializando banco de dados do Railway ===")
    
    # Criar categorias
    print("\n1. Criando categorias...")
    initialize_categories()
    
    print("\n=== Processo concluído! ===")

if __name__ == '__main__':
    main()