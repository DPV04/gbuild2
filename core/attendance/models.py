from django.db import models
from django.db import models

class AttendanceRecord(models.Model):
  student_name = models.CharField(max_length=100)
  attendance_status = models.CharField(max_length=20, choices=[
      ('present', 'Present'),
      ('absent', 'Absent'),
      ('excused', 'Excused'),
  ])
  date = models.DateField(auto_now_add=True)  # Automatically set on record creation

  def __str__(self):
    return f"{self.student_name} - {self.attendance_status} ({self.date})"


# Create your models here.
