from django import forms
from .models import Bid

class BidForm(forms.Form):
    bid = forms.DecimalField(max_digits=10, decimal_places=3,required=True)