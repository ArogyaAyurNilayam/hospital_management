# Generated by Django 5.0.3 on 2024-04-28 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacist', '0004_medicine_limit'),
        ('receptionist', '0011_consultation_details_is_consulted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_amount', models.BigIntegerField(blank=True)),
                ('op_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receptionist.consultation_details')),
            ],
        ),
    ]
