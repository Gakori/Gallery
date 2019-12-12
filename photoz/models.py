from django.db import models

class Image(models.Model):
    image_title = models.CharField(max_length=30)
    image_description = models.TextField(max_length=100)
    image_category = models.CharField(max_length=30)
    image_location = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.image_title
