from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Import for login requirement
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required






@login_required(login_url='/login/')
def dexpense(request):
  if request.method == 'POST':
    form = ExpenseForm(request.POST)
    if form.is_valid():
      
      domain = form.cleaned_data['domain']
      description = form.cleaned_data['description']
      amount = int(form.cleaned_data['amount'])
    

      Expense.objects.create(
          domain=domain,
          description=description,
          amount=amount
      )
      
      # Redirect to expense list after successful save
  else:
    form = ExpenseForm()

  expenses=Expense.objects.all()  
  totalspent = sum(expense.amount for expense in expenses)

#   totalspent=str(totalspent)
  context = {'form': form , 'expenses':expenses , 'totalspent':totalspent}
  return render(request, 'expenses.html', context)


# Create your views here.
