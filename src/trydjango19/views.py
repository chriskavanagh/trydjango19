from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserSignInForm, UserRegistrationForm


# ---------views------------#
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
    
    
def sign_up(request):
    form = UserRegistrationForm(request.POST or None)
    print form
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, 'User Was Successfully Created')
        return redirect('home')
    cxt = {'form': form}
    return render(request, 'sign_up.html', cxt)
    
    
# def user_login(request):
    # form = UserSignInForm(request.POST or None)
    # if form.is_valid():
        # cd = form.cleaned_data
        # username = cd['username']
        # password = cd['password']
        # user = authenticate(username=username, password=password)
        # if user is not None and user.is_active:
            # login(request, user)
            # return redirect('list')
        # else:
            # message.warning(request, 'Your Account Is Disabled')
    # return render(request, 'base.html', {'form': form})
                
            