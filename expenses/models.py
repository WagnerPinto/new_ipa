from django.db import models
from expense_account.models import ExpenseAccount
from suppliers.models import Supplier
from affiliates.models import Affiliate


class Expense(models.Model):
    account = models.ForeignKey(ExpenseAccount, on_delete=models.PROTECT, related_name='expense_account')
    document_number = models.CharField(max_length=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='exp_suppliers')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField()
    center_cost = models.ForeignKey(Affiliate, on_delete=models.PROTECT, null=True, blank=True, related_name='cost_center')
    observation = models.TextField(max_length=250, blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(self.account)
