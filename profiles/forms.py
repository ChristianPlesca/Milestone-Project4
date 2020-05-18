from django import forms
from .models import UserProfile


# Edit Profile Form
class ImageProfileForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = UserProfile
        fields = ('description', 'city', 'website', 'phone', 'image')