from django.db import models

class Affiliate(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField()
    description = models.TextField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.name
