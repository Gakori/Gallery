from django.contrib import admin
from .models import Image,Category,Location,tags

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal=('tags')

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)