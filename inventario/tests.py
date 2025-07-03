from django.test import TestCase

from .models import Categoria


class TestCategoria(TestCase):
    # fixtures = ['dump_inventario.json']

    def test_grabacion(self):
        q =  Categoria(nombre="Bebidas")
        q.save()
        self.assertEqual(Categoria.objects.count(), 1)
