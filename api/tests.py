from django.test import TestCase
from django.urls import reverse
from .models import Producto, Cliente, Pedido
from .forms import ProductoForm
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm
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
        self.assertEqual(cliente.nombre, 'Pedro')
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



class RegistroUsuarioTestCase(TestCase):
    def test_registro_usuario_form(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = RegistroUsuarioForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registro_usuario_view(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = self.client.post(reverse('registro_usuario'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

class ListarUsuariosTestCase(TestCase):
    def test_listar_usuarios_view(self):
        User.objects.create_user(username='user1', password='password123')
        response = self.client.get(reverse('listar_usuarios'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_usuarios.html')
        self.assertIn('usuarios', response.context)
        self.assertEqual(len(response.context['usuarios']), 1)

class BuscarProductoTestCase(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(codigoProducto='12345', nombre='Producto1')

    def test_buscar_producto_view(self):
        response = self.client.post(reverse('buscar_producto'), {'codigo': '12345'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'buscar_producto.html')
        self.assertIn('productos', response.context)
        self.assertEqual(len(response.context['productos']), 1)
        self.assertEqual(response.context['productos'][0].codigoProducto, '12345')

class IntegracionRegistroListarUsuariosTestCase(TestCase):
    def test_registro_y_listar_usuarios(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        self.client.post(reverse('registro_usuario'), data=form_data)
        response = self.client.get(reverse('listar_usuarios'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', [user.username for user in response.context['usuarios']])

class IntegracionRegistroBuscarProductoTestCase(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(codigoProducto='12345', nombre='Producto1')

    def test_registro_y_buscar_producto(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        self.client.post(reverse('registro_usuario'), data=form_data)
        response = self.client.post(reverse('buscar_producto'), {'codigo': '12345'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Producto1', [producto.nombre for producto in response.context['productos']])
