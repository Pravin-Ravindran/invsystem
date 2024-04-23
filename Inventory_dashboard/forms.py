from django import forms

from .models import Order

# Created a class which holds order model and mentions the fields to be rendered in the form 
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'category' , 'quantity']
        