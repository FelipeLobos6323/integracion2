from django.test import TestCase
from django.urls import reverse
from .models import Producto, Cliente, Pedido
from .forms import ProductoForm

#Pruebas de integracion
class ProductoModelTest(TestCase):
    def test_crear_producto_post(self):
        """
        Prueba que la vista de creación de producto cree un nuevo producto con datos válidos en una solicitud POST.
        """
        data = {
            'codigoProducto': '123456',
            'marca': 'MarcaPrueba',
            'codigo': 'CP1234',
            'nombre': 'Producto de prueba',
            'precio': '10990',
            'fecha': '2023-01-01',
            'disponible': True,
            'stock': 100
        }
        response = self.client.post(reverse('crear_producto'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Producto.objects.count(), 1)
        self.assertRedirects(response, reverse('listar_productos'))
        
        # Verificar que el producto fue creado con los datos correctos
        producto = Producto.objects.first()
        self.assertEqual(producto.codigoProducto, '123456')
        self.assertEqual(producto.marca, 'MarcaPrueba')
        self.assertEqual(producto.codigo, 'CP1234')
        self.assertEqual(producto.nombre, 'Producto de prueba')
        
        # Introducir error: Cambiar el precio esperado para que falle la prueba
        self.assertEqual(producto.precio, '3921')
        
        self.assertEqual(producto.fecha, '2023-01-01')
        self.assertTrue(producto.disponible)
        self.assertEqual(producto.stock, 100)

class ClienteModelTest(TestCase):
    def test_creacion_cliente(self):
        cliente = Cliente.objects.create(
            rut='12345678-9',
            nombre='Juan',
            apellido='Pérez',
            email='juan@example.com',
            direccion='Calle Falsa 123'
        )
        self.assertEqual(cliente.nombre, 'Juan')
        self.assertEqual(cliente.email, 'juan@example.com')
class PedidoModelTest(TestCase):
    def test_creacion_pedido(self):
        producto = Producto.objects.create(
            codigoProducto='123456',
            marca='MarcaPrueba',
            codigo='CP1234',
            nombre='jugo',
            precio='10.99',
            fecha='2023-01-01',
            disponible=True,
            stock=100
        )
        pedido = Pedido.objects.create(
            rut='12345678-9',
            nombre='Juan',
            apellido='Pérez',
            email='juan@example.com',
            direccion='Calle Falsa 123',
            producto=producto,
            cantidad=10
        )
        self.assertEqual(pedido.nombre, 'Juan')
        self.assertEqual(pedido.producto.nombre, 'leceh')

    def test_valores_predeterminados_producto(self):
        producto = Producto.objects.create(
            codigoProducto='123456',
            marca='MarcaPrueba',
            codigo='CP1234',
            nombre='Producto con valores predeterminados',
            precio='10.99',
            fecha='2023-01-01'
        )
        self.assertFalse(producto.disponible)
        self.assertEqual(producto.stock, 0)
    def test_valores_predeterminados_pedido(self):
        producto = Producto.objects.create(
            codigoProducto='123456',
            marca='MarcaPrueba',
            codigo='CP1234',
            nombre='Producto de prueba',
            precio='10.99',
            fecha='2023-01-01',
            disponible=True,
            stock=100
        )
        pedido = Pedido.objects.create(
            rut='12345678-9',
            nombre='Juan',
            apellido='Pérez',
            email='juan@example.com',
            direccion='Calle Falsa 123',
            producto=producto,
            cantidad=10
        )
        self.assertFalse(pedido.completado)

#Pruebas unitarias
class CrearProductoViewTest(TestCase):
    def test_crear_producto_post(self):
        data = {
            'codigoProducto': '123456',
            'marca': 'MarcaPrueba',
            'codigo': 'CP1234',
            'nombre': 'Producto de prueba',
            'precio': '10.99',
            'fecha': '2023-01-01',
            'disponible': True,
            'stock': 100
        }
        response = self.client.post(reverse('crear_producto'), data)
        self.assertEqual(response.status_code, 302)
        
        # Introducir error: cambiar la URL de redirección esperada
        self.assertRedirects(response, reverse('listar_productos_incorrecto'))
        
        self.assertEqual(Producto.objects.count(), 1)

class ListarProductosViewTest(TestCase):
    def test_listar_productos(self):
        Producto.objects.create(
            codigoProducto='123456',
            marca='MarcaPrueba',
            codigo='CP1234',
            nombre='Producto de prueba',
            precio='10.99',
            fecha='2023-01-01',
            disponible=True,
            stock=100
        )
        response = self.client.get(reverse('listar_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_productos.html')
        
        # Introducir error: cambiar el contenido esperados
        self.assertContains(response, 'cosa erronea')


class EditarProductoViewTest(TestCase):
    def test_editar_producto(self):
        producto = Producto.objects.create(
            codigoProducto='123456',
            marca='MarcaPrueba',
            codigo='CP1234',
            nombre='Producto de prueba',
            precio='10.99',
            fecha='2023-01-01',
            disponible=True,
            stock=100
        )
        data = {
            'codigoProducto': '123456',
            'marca': 'MarcaEditada',
            'codigo': 'CP1234',
            'nombre': 'Producto editado',
            'precio': '12.99',
            'fecha': '2023-01-01',
            'disponible': True,
            'stock': 50
        }
        response = self.client.post(reverse('editar_producto', args=[producto.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_productos'))
        producto.refresh_from_db()
        self.assertEqual(producto.marca, 'MarcaEditada')
        self.assertEqual(producto.nombre, 'Producto editado')
class EliminarProductoViewTest(TestCase):
    def test_eliminar_producto(self):
        producto = Producto.objects.create(
            codigoProducto='123456',
            marca='MarcaPrueba',
            codigo='CP1234',
            nombre='Producto de prueba',
            precio='10.99',
            fecha='2023-01-01',
            disponible=True,
            stock=100
        )
        response = self.client.post(reverse('eliminar_producto', args=[producto.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_productos'))
        self.assertEqual(Producto.objects.count(), 0)
class ConsultarPreciosViewTest(TestCase):
    def test_consultar_precios(self):
        Producto.objects.create(
            codigoProducto='123456',
            marca='MarcaPrueba',
            codigo='CP1234',
            nombre='Producto de prueba',
            precio='10.99',
            fecha='2023-01-01',
            disponible=True,
            stock=100
        )
        response = self.client.get(reverse('consultar_precios'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'consultar_precios.html')
        self.assertContains(response, '10.99')
        self.assertContains(response, 'Producto de prueba')

