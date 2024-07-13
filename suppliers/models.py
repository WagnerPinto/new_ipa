from django.db import models
from states.models import State


class Supplier(models.Model):

    name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18)
    city = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='states')

    def __str__(self):
        return self.name
