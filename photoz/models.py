from django.db import models

class Image(models.Model):
    image_title = models.CharField(max_length=30)
    image_description = models.TextField(max_length=100)
    image_category = models.CharField(max_length=30)
    image_location = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to='images/')
    
    @classmethod
    def search_by_category(cls,category):
        images = cls.objects.filter(category__name__icontains=category)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location
    
    def __str__(self):
        return self.image_title

class Category(models.Model):
    title = models.CharField(max_length=30),
    
    def __str__(self):
        return f'name: {self.name}'
    
    
class Location(models.Model):
    place = models.CharField(max_length=150)
    
    def __str__(self):
        return f'place: {self.place}'
    