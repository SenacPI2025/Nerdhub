from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'nucleo/index.html')

def ver_carrinho(request):
    return HttpResponse("Carrinho ainda não implementado.")

def sobre(request):
    return HttpResponse("Página Sobre - temporária")

def suporte(request):
    return HttpResponse("Página de Suporte - temporária")

