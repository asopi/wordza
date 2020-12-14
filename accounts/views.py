from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from .forms import CustomeUserCreationForm


@unauthenticated_user
def register_view(request):
    """
    Takes request and returns the rendered view which includes the registration form.
    In case of POST, a new user will be created and redirected to the login page.
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
    Takes the request and returns the login form. In case of POST, the user will be logged in.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password is incorrect')
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
