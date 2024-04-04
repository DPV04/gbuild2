from django import forms
from .models import marks
class marksinput(forms.Form):
    sem=forms.CharField(max_length=200)
    sub1marks=forms.DecimalField(max_digits=10, decimal_places=2,label="sub1marks")
    sub2marks=forms.DecimalField(max_digits=10, decimal_places=2,label="sub2marks")
    sub3marks=forms.DecimalField(max_digits=10, decimal_places=2,label="sub3marks")