from django.db import models



class Expense(models.Model):
  domain=models.CharField(max_length=20, choices=[
      ('Education', 'Education'),
      ('Resources', 'Resources'),
      ('dailyneed', 'Dailyneed'),
  ])
  description = models.CharField(max_length=200)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  date = models.DateTimeField(auto_now_add=True)
  
  

  def __str__(self):
    return f"{self.description} ({self.date})"

# Create your models here.
