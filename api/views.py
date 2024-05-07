from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from rest_framework import viewsets
from .serializer import ProductoSerializer
from .models import Producto
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
import random


# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class = ProductoSerializer
    


    
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})    

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



#-------------------VISTA CLIENTE CONSULTAR PRECIO-----------------
def consultar_precios(request):
    # Obtener todos los productos
    productos = Producto.objects.all()
    # Crear una lista de precios de productos
    precios = [{'nombre': producto.nombre, 'precio': producto.precio, 'marca': producto.marca} for producto in productos]
    # Renderizar la plantilla con la lista de precios
    return render(request, 'consultar_precios.html', {'precios': precios})
    
    