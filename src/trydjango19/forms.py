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
    email = forms.EmailField(required=True)        
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user      
        
           
class UserRegistrationForm(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout('username', 'email', 'password1', 'password2',
                                ButtonHolder(Submit('register','Register',
                                                css_class='btn-primary')))