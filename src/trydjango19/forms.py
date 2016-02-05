from __future__ import absolute_import
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignInForm(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout('username', 'password1', 'password2',
                                ButtonHolder(Submit('register','Register',
                                                css_class='btn-primary')))