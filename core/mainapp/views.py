from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout

# Create your views here.


def login_page(request):
    
  if request.method == "POST":
     data=request.POST

     username=data.get('username')
     password=data.get('password')

     if not User.objects.filter(username=username):
        messages.info(request,"u are an impposter")
        return redirect("/login/")
 
     user=authenticate(username = username,password = password)

     if user is None:
        messages.info(request,"invalid password")
        return redirect('/login/')

     else:
        login(request,user)
        return redirect("/home/")   
        
  return render(request , 'login.html')

def logout_page(request):
   logout(request)

   # @login_required(login_url='/login/')
   return redirect('/login/')

@login_required(login_url='/login/')
def home(request):
   return render(request,'home.html')

@login_required(login_url='/login/')
def reminders(request):
   return render(request,'mm.html')