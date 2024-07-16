from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required




def profile(requset):
    return render(requset, 'profile.html', {})

def home(requset):
    return render(requset, 'base.html', {})


