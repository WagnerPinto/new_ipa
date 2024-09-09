from django.db import models
from orders.models import Order
from expenses.models import Expense
from banks.models import Bank
from cards.models import Card

PAYMENT_OPTIONS = (
    ("Bank Slip", "BANK SLIP"),
    ("credit", "CREDIT CARD"),
    ("debit", "DEBIT CARD"),
    ("Pix", "PIX"),
    ("Ted", "TED"),
    ("Cash", "CASH"),
    ("Check", "CHECK"),
    ("Deposit", "DEPOSIT"),
    ("Debit Bank", "DEBIT BANK"),
)


class Payment(models.Model):
    type = models.CharField(choices=PAYMENT_OPTIONS, max_length=120)
    payment_date = models.DateField()
    payment_order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True, related_name='pay_order')
    payment_expense = models.ForeignKey(Expense, on_delete=models.PROTECT, null=True, blank=True, related_name='pay_expense')
    payment_bank = models.ForeignKey(Bank, on_delete=models.PROTECT, null=True, blank=True, related_name='payment_bank')
    payment_card = models.ForeignKey(Card, on_delete=models.PROTECT, null=True, blank=True, related_name='pay_card')
    paid_value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.type)
