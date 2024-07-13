from django.contrib import admin
from . models import Product


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'register_date')
    search_fields = ('name', 'register_date')

    admin.site.register(Product)