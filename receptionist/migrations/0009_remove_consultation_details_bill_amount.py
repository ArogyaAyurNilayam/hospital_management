# Generated by Django 5.0.3 on 2024-04-27 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0008_alter_consultation_details_op_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation_details',
            name='bill_amount',
        ),
    ]
