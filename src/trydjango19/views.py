from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserSignInForm

# Views
def HomePageView(request):
    return render(request, 'home.html', {})
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('list')
            else:
                message.warning(request, 'Your Account Is Disabled')
        else:
            message.warning(request, 'Please Provide A Valid Username Or Password')
            
            
@login_required           
def user_logout(request):
    logout(request)
    return redirect('home')
                
            