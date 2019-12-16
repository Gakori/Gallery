from django.test import TestCase
from .models import Image,Category,Location

class ImageTestClass(TestCase):
    def setUp(self):
        self.image=Image(image_title='Liam',image_description='My friend is the most important person')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Liam,Image))
        
    def test_save_method(self):
        self.Liam.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) >0)
        
