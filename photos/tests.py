from django.test import TestCase
from .models import Category

# Create your tests here.
class CategoryTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.design=Category(name='Design')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.design,Category))

    #Testing Save Method
    def test_save_method(self):
        self.design.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_method(self):



        self.design.save_category()
        self.design.delete_category()

