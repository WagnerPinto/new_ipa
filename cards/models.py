from django.db import models

class Card(models.Model):
    card_number = models.CharField(max_length=17)
    flag = models.CharField(max_length=30)
    owner = models.CharField(max_length=150)
    due_date = models.CharField(max_length=2)
    validate_date = models.CharField(max_length=5)
    limit_credit = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return str(self.card_number)
