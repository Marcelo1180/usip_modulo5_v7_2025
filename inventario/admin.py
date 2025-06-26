from django.contrib import admin

from .models import Categoria, Producto

admin.site.register(Categoria)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'unidades', 'disponible')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('disponible',)

admin.site.register(Producto, ProductoAdmin)
