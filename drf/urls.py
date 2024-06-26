"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from api import views 




urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/v1', include('api.urls')),
    path('docs/', include_docs_urls(title='Documentacion de api')),
    
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('ver_producto/<int:pk>/', views.ver_producto, name='ver_producto'),
    path('editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('consultar_precios/', views.consultar_precios, name='consultar_precios'),
    path('seleccionar_productos/', views.seleccionar_productos, name='seleccionar_productos'),
    
    path('vendedor/', views.vendedor, name='vendedor'),
    #----------CONSULTAR PRECIO CLIENTE---------
    path('pedidos_pendientes/', views.pedidos_pendientes, name='pedidos_pendientes'),
    path('procesar_compra/', views.procesar_compra, name='procesar_compra'),
    path('eliminar_pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    #----------Crear usuario--------------------#
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    #----------Buscar producto por codigo-------
    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),
    path('vista_administrador/', views.vista_administrador, name='vista_administrador'),
    
    
]
