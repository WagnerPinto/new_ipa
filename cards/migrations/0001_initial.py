# Generated by Django 5.0.6 on 2024-07-08 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=17)),
                ('flag', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=150)),
                ('due_date', models.CharField(max_length=2)),
                ('validate_date', models.CharField(max_length=5)),
                ('limit_credit', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
