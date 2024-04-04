from django.db import models

from django.db import models



class marks(models.Model):
    sem=models.CharField(max_length=200)
    sub1marks=models.DecimalField(max_digits=10, decimal_places=2)
    sub2marks=models.DecimalField(max_digits=10, decimal_places=2)
    sub3marks=models.DecimalField(max_digits=10, decimal_places=2)

