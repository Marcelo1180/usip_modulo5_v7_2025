from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view

from .forms import ProductoForm
from .models import Categoria, Producto
from .serializers import (CategoriaSerializer, ContactSerializer,
                          ProductoSerializer, ReporteProductosSerializer)


def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

def categorias(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get('nombre')
    # import pdb; pdb.set_trace()

    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        categorias = Categoria.objects.all()

    return render(request, 'form_categorias.html', {
        "categorias": categorias
    })

def productoFormView(request):
    form = ProductoForm()
    producto = None

    id_producto = request.GET.get('id')
    if id_producto:
        producto = get_object_or_404(Producto, id=id_producto)
        form = ProductoForm(instance=producto)

    if request.method == 'POST':
        if producto:
            form = ProductoForm(request.POST, instance=producto)
        else:
            form = ProductoForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, 'form_productos.html', {
        "form": form
    })

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@api_view(['GET'])
def categoria_count(request):
    try:
        cantidad = Categoria.objects.count()
        return JsonResponse({
                'cantidad': cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


@api_view(['GET'])
def productos_en_unidades(request):
    try:
        productos = Producto.objects.filter(unidades='u')
        return JsonResponse(
            ProductoSerializer(productos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)

@api_view(['GET'])
def reporte_productos(request):
    try:
        productos = Producto.objects.filter(unidades='u')
        cantidad = productos.count()
        return JsonResponse(
            ReporteProductosSerializer({
                "cantidad": cantidad,
                "productos": productos,
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


@api_view(['POST'])
def enviar_mensaje(request):
    cs = ContactSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse({'message': 'Mensaje enviado correctamente'},
                            status=200)
    else:
        return JsonResponse({'message': cs.errors}, status=200)
