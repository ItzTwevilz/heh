from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, TestForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import TestModel

def homepage(request):

    return render(request, 'main/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context = {'registerform': form}
    return render(request, 'main/register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'loginform':form}
    return render(request, 'main/my-login.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect("")

@login_required(login_url="my_login")
def dashboard(request):

    return render(request, 'main/dashboard.html')

@login_required(login_url="my_login")
def main(request):

    return render(request, 'main/main.html')

@login_required(login_url="my_login")
def registration(request):
    form = TestForm()
    context = {'choice':form}
    return render(request, 'main/registration.html', context=context)