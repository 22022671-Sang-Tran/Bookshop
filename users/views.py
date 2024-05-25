from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import logout as auth_logout, update_session_auth_hash
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

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
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

@login_required 
def dashboard(request):
    return render(request, 'users/dashboard.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = request.user
        user.username = username
        user.email = email

        if password and password == confirm_password:
            user.set_password(password)
            update_session_auth_hash(request, user)  # Important, to keep the user logged in after password change

        user.save()
        
        messages.success(request, 'Your profile was successfully updated!')
        return redirect('dashboard')

    return render(request, 'users/edit_profile.html')
