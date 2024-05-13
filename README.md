# integracion2

# En este repositorio hicimos una Rest Framework que contiene una API REST
# Para poder ejecutar el repositorio tenemos que ir a Visual Studio Code,
# Luego tenemos que abrir una Nueva Terminal,Después colocaremos el siguiente comando: pip install -r requirements.txt con este comando instalaremos todas las dependencias utilizadas 
# en el repositorio posteriormente colocaremos el siguiente comando: python manage.py runserver y se ejecutará el repositorio.
# Cuando este listo tendremos que ir a nuestro navegador y colocar la siguiente ip : http://127.0.0.1:8000/
# Al momento de entrar en la url tenemos 4 vistas disponibles que son Administrador, Vendedor, Bodeguero y Cliente.
# En la vista Administrador tenemos el listado de productos junto con su información y también podemos integrar nuevos productos al seleccionar "Crear Producto",
# Al ingresar tenemos que rellenar el formulario y Apretar Guardar. Despues de ello, se refleja después en la vista de administrador, tambien en la parte derecha podemos reflejar
# Botones "Editar" que podemos modificar la informacion del producto y el boton "Eliminar" para descartar el producto de la base de datos,
# En la vista Vendedor tenemos un formulario para hacer una venta para un cliente y también visualizamos los productos que contiene "FERREMAS", al momento de rellenar el formulario
# Apretamos el boton "Comprar" para mandar una solicitud hacia el bodeguero para revisar si estan los productos en stock. 
# En la vista de bodeguero podemos reflejar los pedidos de los clientes y poder revisar si es que hay en stock disponible, En la parte derecha podemos reflejar unos
# botones que son "Pedido con stock" que al momento de tener stock disponible se apreta el boton para mandar la informacion y poder realizar el despacho, y el boton de
# "Pedido sin stock" que significa que no hay stock disponible y se elimina el formulario. 
# En la vista cliente podemos reflejar el nombre del producto, marca del producto y el precio correspondiente.
# Y para revisar la documentación de la API REST debes ingresar a esta url : http://127.0.0.1:8000/docs/
# También tenemos otro apartado de Django REST Framework para ingresar algún producto nuevo a "FERREMAS" ingresando esta url: http://127.0.0.1:8000/api/v1Producto/,                #   podemos visualizar los productos creados en la base de datos, en el apartado de abajo podemos visualizar tambien la información para poder crear un producto y al ingresar "POST",  se ingresa a la base de datos
