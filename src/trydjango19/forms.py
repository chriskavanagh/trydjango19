from __future__ import absolute_import
from django import forms
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

class UserSignInForm(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)