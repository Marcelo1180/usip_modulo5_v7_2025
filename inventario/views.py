from django.http import HttpResponse
from django.shortcuts import render

from .models import Categoria


def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {
        "categorias": categorias
    })
