from django.db import models
from states.models import State

class Bank(models.Model):
    name = models.CharField(max_length=150)
    account = models.CharField(max_length=20)
    agency = models.CharField(max_length=30)
    city = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='estado')
    manager = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self):
        return self.name
