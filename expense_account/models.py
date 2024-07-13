from django.db import models


class ExpenseAccount(models.Model):
    account = models.CharField(max_length=150)
    description = models.TextField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.account
