from django.db import models
from django import forms
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
    



class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)  # Indicador de personal interno
    is_active = models.BooleanField(default=True)  # Indicador de cuenta activa

    def __str__(self):
        return self.username
    
class UserCreationForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        user = User.objects.create_user(username=username, email=email, password=password)
        return user