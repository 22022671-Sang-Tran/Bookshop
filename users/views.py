from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import logout as auth_logout
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are now registered and can login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')
