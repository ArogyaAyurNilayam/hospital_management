# Generated by Django 5.0.3 on 2024-04-28 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacist', '0006_medicine_bill_amount_delete_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='bill_amount',
        ),
    ]
