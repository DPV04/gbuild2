# from django.shortcuts import render, redirect
# from django.views.generic import TemplateView, ListView, CreateView
# from django.core.files.storage import FileSystemStorage
# from .forms import *
# from django.contrib.auth.decorators import login_required
# @login_required(login_url='/login/')
# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#     return render(request, 'upload.html', context)


# @login_required(login_url='/login/')
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'book_list.html', {
#         'books': books
#     })
# @login_required(login_url='/login/')
# def upload_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'upload_book.html', {
#         'form': form
#     })

from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
# from django.http import HttpResponse

# def index(request):
#     return render(request,'index.html')
# Create your views here.
@login_required(login_url='/login/')
def students(request):
    if request.method == "POST":

        data = request.POST

        name = data.get("name")
        subject = data.get("address")
        image = request.FILES.get("image")


        student.objects.create( name=name,
            subject=subject,
            image=image,
        )

        # queryset.save()

        return redirect('/resources/students/')
    
    queryset=student.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(name__icontains= request.GET.get("search"))

    context={'rece':queryset}
    return render(request,'base.html',context)