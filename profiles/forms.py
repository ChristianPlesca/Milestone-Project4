from django import forms
from .models import UserProfile



class ImageProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('description', 'city', 'website', 'phone','image')