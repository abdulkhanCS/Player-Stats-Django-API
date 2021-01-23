from django.db import models
from django.conf import settings

# Create your models here.

class PlayerStats(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.CharField(max_length=10)