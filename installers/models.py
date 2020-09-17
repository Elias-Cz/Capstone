from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    installer = models.BooleanField(default=False)
    pass

class Date(models.Model):
    taken = models.BooleanField(default=False)

class Schedule(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name="date")
