from django.db import models


class State(models.Model):
    uf = models.CharField(max_length=2)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.uf
