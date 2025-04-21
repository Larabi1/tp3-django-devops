from django.test import TestCase
from .models import MyModel

class MyModelTest(TestCase):
    def setUp(self):
        MyModel.objects.create(name="test_name")

    def test_model_name(self):
        test_model = MyModel.objects.get(name="test_name")
        self.assertEqual(str(test_model), "test_name")
