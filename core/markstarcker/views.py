from django.shortcuts import render , redirect
from .forms import *
from.models import *
# Create your views here.
def index(request):

    form = marksinput()
    if request.method == 'POST':
        form= marksinput(request.POST)
        if form.is_valid:
            form.save()

            marks.objects.create(
                
            )

            return redirect('/main/')
        queryset=marks.objects.all()

        # context={
        #     'form':form
        #     # 'queryset':queryset
        # }
        
        
    return render(request,'main.html', {'form':form,'queryset':queryset})

# def main(request):
#     return render(request,'main.html')