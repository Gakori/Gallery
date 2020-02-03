from django.db import models
import pyperclip

class Image(models.Model):
    image_title = models.CharField(max_length=30)
    image_description = models.TextField(max_length=100)
    image_category = models.CharField(max_length=30)
    image_location = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.image_title
    
    def save_image(self):
        self.save()
        
    class Meta:
        ordering = ['image_title']
        
    def update_image(slef,image_title=image_title,image_category=None):
        self.image_title=image_title if image_title else self.image_category
    
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def search_by_category(cls,category):
        images = cls.objects.filter(image_category__icontains=category)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__title=location).all()
        return image_location
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def copy_image(cls, image_url):
        pyperclip.copy(image_url)
    
class tags(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    image_title = models.CharField(max_length=30)
    description = models.TextField(max_length=30)

    # @classmethod
    # def search_by_category(cls,search_term):
    #     category = cls.objects.filter(image_title__icontains=search_term)
    #     return category
    
    def __str__(self):
        return f'title: {self.title}'
    
class Location(models.Model):
    place = models.CharField(max_length=150)
    
    def __str__(self):
        return f'place: {self.place}'
    
  