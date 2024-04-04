from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/login/')
def chats(request):
    return render(request, 'chat.html')