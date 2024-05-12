from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producto (models.Model):
    codigoProducto = models.CharField(max_length=100)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=10)
    fecha = models.CharField(max_length=10)
    disponible = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)


class Cliente(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    
class Pedido(models.Model):
    rut = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    completado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.producto.nombre}"