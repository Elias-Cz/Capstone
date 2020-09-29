from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    installer = models.BooleanField(default=False)
    day = models.CharField(max_length=140, blank=True)
    pass

class Day(models.Model):
    day_data = models.CharField(max_length=140)
    installer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="installer_day")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_day")
    def __str__(self):
        return f"{self.customer} has an appointment on {self.day_data}, with installer {self.installer} at 10am"
class Schedule(models.Model):
    date_data = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="date_data")
    user_appointment = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_appointment")
    def __str__(self):
        return f"{self.date_data}"
