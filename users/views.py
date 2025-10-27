from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed

def login(request):
    '''Log a user in'''
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            """do smt"""
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'users/login.html', context)

def signup(request):
    '''create a new user'''
    if request.method != 'POST':
        # display a blank form
        form = UserCreationForm()
    else:
        # data is submitted, methos is post
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    context = {'form':form}
    return render(request, 'users/signup.html', context)

@login_required
def log_out(request):
    '''Just return the logout page'''
    return render(request, 'users/loggedout.html')