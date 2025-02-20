# Generated by Django 5.1.4 on 2025-01-18 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0014_alter_consultation_details_diagnosis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientregistration',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
