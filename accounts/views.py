from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from .forms import CustomeUserCreationForm


@unauthenticated_user
def register_view(request):
    """
    Takes unauthorized request and returns the rendered view which includes the registration form.
    If the user is already logged in, he will be redirected to the dashboard.
    """
    form = CustomeUserCreationForm()
    if request.method == 'POST':
        form = CustomeUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account was created for { username }")
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def login_view(request):
    """
    Takes the unauthorized request and returns the login form.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
