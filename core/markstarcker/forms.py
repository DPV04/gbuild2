from django import forms
from .models import marks
class marksinput(forms.ModelForm):
    class Meta:
        model=marks
        fields="__all__"