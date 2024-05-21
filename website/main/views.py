from django.shortcuts import render, redirect
from . forms import AuthenticationForm, TestForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import IdentityModel

def homepage(request):

    return render(request, 'main/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        initial_data = {'username': '', 'password': ''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'main/my-login.html', {'form': form})

def user_logout(request):
    auth.logout(request)
    return redirect("./login")

@login_required(login_url="login")
def dashboard(request):

    return render(request, 'main/dashboard.html')

@login_required(login_url="login")
def main(request):

    return render(request, 'main/main.html')

@login_required(login_url="login")
def registration(request):
    form = TestForm()
    context = {'choice':form,
               'eduChoice':form,
               'fparent':form,
               'socialStatus':form,}
    return render(request, 'main/registration.html', context=context)