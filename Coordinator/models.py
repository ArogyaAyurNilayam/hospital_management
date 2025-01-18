from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.
class User(AbstractUser):
    Designation=models.CharField(max_length=15)
    phone=models.BigIntegerField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)


