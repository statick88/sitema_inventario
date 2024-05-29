from django.test import TestCase
from .models import Producto

class ProductoTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        Producto.objects.create(nombre='camisa', precio=100.00, cantidad=2)

    def test_name_content(self):
        my_model = Producto.objects.get(id=1)
        expected_object_name = f'{my_model.nombre}'
        excepted_object_precio = f'{my_model.precio}'
        excepted_object_cantidad = f'{my_model.cantidad}'
        self.assertEqual(expected_object_name, 'camisa')
        self.assertEqual(excepted_object_precio, '100.00')
        self.assertEqual(excepted_object_cantidad, '2')