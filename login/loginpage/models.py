from django.db import models

# Create your models here.
# YourAppName/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
