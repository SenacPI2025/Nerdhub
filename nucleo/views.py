from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'nucleo/index.html')

def ver_carrinho(request):
    return HttpResponse("Carrinho ainda não implementado.")