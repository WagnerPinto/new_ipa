# Generated by Django 5.0.6 on 2024-07-08 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('banks', '0001_initial'),
        ('cards', '0001_initial'),
        ('expenses', '0002_expense_center_cost'),
        ('orders', '0003_alter_order_order_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('credit', 'CREDIT CARD'), ('debit', 'DEBIT CARD'), ('Pix', 'PIX'), ('Ted', 'TED'), ('Cash', 'CASH'), ('Check', 'CHECK'), ('Deposit', 'DEPOSIT'), ('Debit Bank', 'DEBIT BANK')], max_length=120)),
                ('payment_date', models.DateField()),
                ('paid_value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payment_bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='payment_bank', to='banks.bank')),
                ('payment_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pay_card', to='cards.card')),
                ('payment_expense', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pay_expense', to='expenses.expense')),
                ('payment_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pay_order', to='orders.order')),
            ],
        ),
    ]
