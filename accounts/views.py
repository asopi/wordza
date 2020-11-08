from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user
from .forms import CustomeUserCreationForm


@unauthenticated_user
def registerView(request):
    form = CustomeUserCreationForm()
    if request.method == 'POST':
        form = CustomeUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # currently not in use
            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            messages.success(request, f"Account was created for { username }")
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    print("123")
    logout(request)
    return redirect('login')
