from django.db import models

# Create your models here.

class Producto (models.Model):
    codigoProducto = models.CharField(max_length=100)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=10)
    fecha = models.CharField(max_length=10)
    