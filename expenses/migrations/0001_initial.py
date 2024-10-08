# Generated by Django 5.0.6 on 2024-07-07 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('expense_account', '0001_initial'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_number', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('due_date', models.DateField()),
                ('observation', models.TextField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='expense_account', to='expense_account.expenseaccount')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exp_suppliers', to='suppliers.supplier')),
            ],
        ),
    ]
