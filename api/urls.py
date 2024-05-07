from django.urls import path,include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'Producto',views.ProductoViewSet)


urlpatterns=[
    path('',include(router.urls)),
    path('listar-productos/', views.listar_productos, name='listar_productos')
    
]