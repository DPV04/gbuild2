from django import forms

class StudentAttendanceForm(forms.Form):
    subject_name = forms.CharField(max_length=100, label="Subject_Name")
    attendance_status = forms.ChoiceField(choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Holiday', 'Holiday'),
    ], label="Attendance Status")
