

# Create your models here.
from django.db import models
from django.contrib.auth.models import*

class student(models.Model):
    
    name =models.CharField(max_length=100)
    subject=models.TextField()
    image=models.FileField()