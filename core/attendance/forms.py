from django import forms

class StudentAttendanceForm(forms.Form):
    student_name = forms.CharField(max_length=100, label="Student Name")
    attendance_status = forms.ChoiceField(choices=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('excused', 'Excused'),
    ], label="Attendance Status")
