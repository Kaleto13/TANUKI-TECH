from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def createacount(request):
    return render(request, 'newacount.html')

def cambiarcontraseña(request):
    return render(request, 'newpassword.html')

def config(request):
    return render(request, 'config.html')