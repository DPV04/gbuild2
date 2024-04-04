from django.shortcuts import render


from django.shortcuts import render , redirect
from .forms import *
from.models import *
# Create your views here.
from django.contrib.auth.decorators import*



@login_required(login_url='/login/')
def index(request):
 form = marksinput()
 sub1marks=0
 sub2marks=0
 sub3marks=0
 total=0
 percent=0
 
 

 if request.method == 'POST':
    form = marksinput(request.POST,'0.0')
    if form.is_valid():
      
      
      sem= form.cleaned_data['sem']
      sub1marks = int(form.cleaned_data['sub1marks'])
      sub2marks = int(form.cleaned_data['sub2marks'])
      sub3marks = int(form.cleaned_data['sub3marks'])
    
      
      marks.objects.create(
          sem=sem,
          sub1marks=sub1marks,
          sub2marks=sub2marks,
          sub3marks=sub3marks,
          
      )
      
      # Redirect to expense list after successful save
    else:
     form = marksinput()

 Marks=marks.objects.all()  
 total = sub1marks+sub2marks+sub3marks
 percent = (total/300)*100

#   totalspent=str(totalspent)
 context = {'form': form , 'Marks':Marks , 'total':total,'percent':percent}
 return render(request, 'studentdetail.html', context)