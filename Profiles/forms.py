from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['picture']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

