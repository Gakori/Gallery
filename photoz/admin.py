from django.contrib import admin
from .models import Image,Category

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal=('tags')

admin.site.register(Image)
admin.site.register(Category)