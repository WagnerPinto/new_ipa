from django.db import models
from category.models import Category

class Product(models.Model):
    
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True ,related_name='categories')
    register_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
