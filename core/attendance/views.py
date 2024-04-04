from django.shortcuts import render, redirect
from .forms import *
from .models import *


def attendance_view(request):
  if request.method == 'POST':
    # Form submitted
    form = StudentAttendanceForm(request.POST)
    if form.is_valid():
      # Process valid form data
      student_name = form.cleaned_data['student_name']
      attendance_status = form.cleaned_data['attendance_status']

      # Save data to database
      AttendanceRecord.objects.create(
          student_name=student_name,
          attendance_status=attendance_status
      )
      message = f"Attendance marked for {student_name} as {attendance_status}"
      # Clear the form for a new entry
      form = StudentAttendanceForm()
  else:
    # Initial form
    form = StudentAttendanceForm()
    message=''

  attendance_records=AttendanceRecord.objects.all()

  context = {'form': form , 'message': message ,'attendance_records':attendance_records }
  return render(request, 'attendance.html', context)

# Create your views here.
