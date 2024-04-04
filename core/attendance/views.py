from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def attendance_view(request):
  if request.method == 'POST':
    # Form submitted
    form = StudentAttendanceForm(request.POST)
    if form.is_valid():
      # Process valid form data
      subject_name = form.cleaned_data['subject_name']
      attendance_status = form.cleaned_data['attendance_status']

      # Save data to database
      AttendanceRecord.objects.create(
          subject_name=subject_name,
          attendance_status=attendance_status
      )
      message = f"Attendance marked for {subject_name} as {attendance_status}"
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
