# base/views.py

from .forms import UserDataForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, 'home.html')

def createacount(request):
    return render(request, 'newacount.html')

def cambiarcontraseña(request):
    return render(request, 'newpassword.html')

def config(request):
    return render(request, 'config.html')



# base/views.py
from django.shortcuts import render
from .forms import UserDataForm
from .models import CustomUser 



def success_page(request):
    return render(request, 'success_page.html')  # Replace 'success_page.html' with your actual template name
def setup_user_data(request):
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
    
    return render(request, 'user_data_form.html', {'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect back to profile view after update
    else:
        form = UserDataForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'profile.html', context)

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')  # Redirect to home or another page after deletion
    return render(request, 'profile.html')

@login_required
def schedule_deletion(request):
    if request.method == 'POST':
        user = request.user
        user.deletion_date = timezone.now() + timezone.timedelta(minutes=1)
        user.save()
        return redirect('home')  # Redirect to home or another page after scheduling
    return render(request, 'profile.html')

.S