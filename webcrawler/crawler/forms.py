from django import forms
from django.contrib.auth.models import User
from . models import UserProfileInfo

class searchform(forms.Form):
    name = forms.CharField()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model =User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    model = UserProfileInfo
    fields=('portfoliosite')