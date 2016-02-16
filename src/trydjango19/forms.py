from __future__ import absolute_import
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignInForm(forms.Form):
    """login form for user"""
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))    
    
    
 # override UserCreationForm and add email. .   
class RegistrationForm(UserCreationForm):
    """extending the UserCreationForm"""
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
        
 
# subclass the RegistrationForm (above), uses crispy_forms. . 
class CrispyRegistrationForm(RegistrationForm):
    """crispy_forms tag for RegistrationForm"""
    def __init__(self, *args, **kwargs):
        super(CrispyRegistrationForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(Fieldset('<h2>Register</h2>', 'username', 'email', 'password1', 'password2'),
                                ButtonHolder(Submit('register','Register',
                                                css_class='btn-primary')))