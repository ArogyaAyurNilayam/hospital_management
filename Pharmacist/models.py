from django.db import models
from receptionist.models import Consultation_details



# Create your models here.
class Medicine(models.Model):
    Name=models.CharField(max_length=30)
    Category=models.CharField(max_length=30)
    Company=models.CharField(max_length=30)
    Rate=models.IntegerField(blank=True, null=True)
    Quantity=models.CharField(max_length=30)
    Number=models.IntegerField(blank=True, null=True)
    is_approved=models.BooleanField(default=0)
    Limit=models.IntegerField(blank=True,null=True)



class Bill_details(models.Model):
    op_number = models.BigIntegerField(unique=False)
    date=models.DateField()
    medicine_name=models.CharField(max_length=30)
    rate=models.IntegerField()
    quantity=models.IntegerField()
    total=models.IntegerField()
    


