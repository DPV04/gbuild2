from django import forms


class ExpenseForm(forms.Form):
 
  domain=forms.ChoiceField(choices=[
      ('Education', 'Education'),
      ('Resources', 'Resources'),
      ('dailyneed', 'Dailyneed'),
      ('miscellaneous','miscellaneous')
  ])
  description = forms.CharField(max_length=200,label="Description")
  amount = forms.DecimalField(max_digits=10, decimal_places=2,label="Amount")


