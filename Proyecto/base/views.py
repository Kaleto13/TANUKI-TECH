# base/views.py

from .forms import UserDataForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
# base/views.py
from django.shortcuts import render
def home(request):
    title = "Home"
    datos = {
        'title': title,
    }

    return render(request, 'base/home.html', datos)

def createacount(request):
    return render(request, 'base/newacount.html')

def cambiarcontraseña(request):
    return render(request, 'base/newpassword.html')

def config(request):
    return render(request, 'base/config.html')







def success_page(request):
    title = "Cuenta creada"
    return render(request, 'base/success_page.html', { 'title': title, }) 

def setup_user_data(request):
    title = "Crear cuenta"

    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)  # Set the password
            user.save()
            messages.success(request, 'User account created successfully.')
            return redirect('success_page')
    else:
        form = UserDataForm()
    
    return render(request, 'base/user_data_form.html', {'form': form, 'title': title})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST, instance=request.user)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect back to profile view after update
    else:
        form = UserDataForm(instance=request.user)
        print(form)
    context = {
        'form': form,
    }
    return render(request, 'base/profile.html', context)

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        print(user)
        print(user, "deleted")
        return redirect('home')  # Redirect to home or another page after deletion
    return render(request, 'base/profile.html')

@login_required
def schedule_deletion(request):
    if request.method == 'POST':
        user = request.user
        user.deletion_date = timezone.now() + timezone.timedelta(minutes=1)
        print(user.deletion_date)
        user.save()
        return redirect('home')  # Redirect to home or another page after scheduling
    return render(request, 'base/profile.html')

def login_view(request):
    title = "Login"

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'base/login.html', {'form': form, 'title': title,})

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')
