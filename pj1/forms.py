from dataclasses import field
from django import forms
from .models import Products,users


class AddProducts(forms.ModelForm):
  class Meta:
    model = Products
    exclude = ['id']
    

class FRegiter(forms.ModelForm):
  class Meta:
    model = users
    # field = '__all__'
    exclude = ['id','status_u']