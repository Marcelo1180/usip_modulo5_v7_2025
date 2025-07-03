from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)

urlpatterns = [
    # path('contact/<str:name>', views.contact, name='contact'),
    # path('categorias', views.categorias, name='categorias'),
    # path('productos', views.productoFormView, name='productos'),
    # path('', views.index, name='index'),

    path('categoria/', views.CategoriaCreateView.as_view(),
         name='categoria-create-list'),
    path('categorias/cantidad/', views.categoria_count, name='categoria-count'),
    path('productos/filtrar/unidades/', views.productos_en_unidades, name='productos-unidades'),
    path('reporte/productos/', views.reporte_productos, name='reporte-productos'),
    path('enviar/mensaje/', views.enviar_mensaje, name='enviar-mensaje'),
    path('', include(router.urls)),
]
