from django.urls import path,include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'Producto',views.ProductoViewSet)


urlpatterns=[
    path('',include(router.urls)),
    path('listar-productos/', views.listar_productos, name='listar_productos'),
    path('detalle_usuario_interno/<int:user_id>/', views.detalle_usuario_interno, name='detalle_usuario_interno'),
    
    
]