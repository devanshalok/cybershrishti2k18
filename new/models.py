from django.db import models
import datetime
from django.utils import timezone

class contact_us(models.Model):
    name = models.CharField(max_length=70)
    email=models.EmailField(default="aaa@bb.c")
    phone=models.IntegerField(default=10)
    message=models.CharField(max_length=500)

    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)

    def __str__(self):
    	return self.name