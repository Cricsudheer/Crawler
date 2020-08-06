from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import UserProfileInfo
from django.contrib.auth.models import User
class searchform(forms.Form):
    name = forms.CharField()

class UserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username', 'email', 'password']

# class UserProfileInfoForm(UserCreationForm):
#     model = UserProfileInfo
#     fields=['portfoliosite']