from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'nucleo/index.html', {'page_name': 'index'})

def ver_carrinho(request):
    return HttpResponse("Carrinho ainda não implementado.")

def sobre(request):
    return render(request, 'nucleo/sobre.html', {'page_name': 'sobre'})

def suporte(request):
    return render(request, 'nucleo/suporte.html', {'page_name': 'suporte'})