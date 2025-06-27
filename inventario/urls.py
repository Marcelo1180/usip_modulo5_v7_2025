from django.urls import path

from . import views

urlpatterns = [
    path('contact/<str:name>', views.contact, name='contact'),
    path('categorias', views.categorias, name='categorias'),
    path('', views.index, name='index'),
]
