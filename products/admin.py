from django.contrib import admin
from .models import Product, ProductsPictures

class PostPictureInline(admin.TabularInline):
    model = ProductsPictures
    fields = ['image']

class PostAdmin(admin.ModelAdmin):
    inlines = [PostPictureInline]

admin.site.register(Product, PostAdmin)
