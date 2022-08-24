from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
 
# Create your views here.
def login_page(request):
    return render(request,'login.html')
from django.contrib.auth import authenticate, login




        
