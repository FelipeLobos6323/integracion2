from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from rest_framework import viewsets
from .serializer import ProductoSerializer
from .models import Producto, Cliente, Pedido
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
import random
from django.http import HttpResponse

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class = ProductoSerializer
    


    
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})    

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})    

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def ver_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'ver_producto.html', {'producto': producto})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

def vendedor(request):
    productos = Producto.objects.all()
    return render(request, 'vendedor.html', {'productos': productos})  



#-------------------VISTA CLIENTE CONSULTAR PRECIO-----------------
def consultar_precios(request):
    # Obtener todos los productos
    productos = Producto.objects.all()
    # Crear una lista de precios de productos
    precios = [{'nombre': producto.nombre, 'precio': producto.precio, 'marca': producto.marca} for producto in productos]
    # Renderizar la plantilla con la lista de precios
    return render(request, 'consultar_precios.html', {'precios': precios})


def pedidos_pendientes(request):
        pedidos = Pedido.objects.filter(completado=False)
        return render(request, 'pedidos_pendientes.html', {'pedidos': pedidos})
    
def procesar_compra(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad'))
        
        producto = Producto.objects.get(pk=producto_id)
        pedido = Pedido.objects.create(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            email=email,
            direccion=direccion,
            producto=producto,
            cantidad=cantidad
        )

        # Redireccionar a la página de pedidos pendientes
        return redirect('vendedor')

         # Renderizar el formulario de compra si no es una solicitud POST
    productos = Producto.objects.all()
    return render(request, 'vendedor.html', {'productos': productos})

def eliminar_pedido(request, pedido_id):
    pedido = Pedido.objects.get(pk=pedido_id)
    pedido.delete()
    # Redireccionar a la página de pedidos pendientes después de eliminar el pedido
    return redirect('pedidos_pendientes')






#------------------- Vista vendedor -------------------------------

def seleccionar_productos(request):
    productos = Producto.objects.all().values('nombre', 'stock')
    return render(request, 'seleccionar_productos.html', {'productos': productos})


    