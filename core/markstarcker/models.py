from django.db import models


class marks(models.Model):
    sub1name=models.CharField(max_length=200)
    sub1marks=models.IntegerField()

    sub2name=models.CharField(max_length=200)
    sub2marks=models.IntegerField()

    sub3name=models.CharField(max_length=200)
    sub3marks=models.IntegerField()



# Create your models here.
