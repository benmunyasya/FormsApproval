from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm    
# Create your views here.
def login_page(request):
    return render(request,'login.html')
from django.contrib.auth import authenticate, login

# def login(request):
#     form_register = UserCreationForm(request.POST)
#     if "register" in request.method == "POST":
       
#         if form_register.is_valid():
#             form_register.save()
#             username = form_register.cleaned_data.get('username')
#             raw_password = form_register.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return render(request, 'login.html', {'form_register': form_register})   
            
#         else:
#              form_register = UserCreationForm()
#     elif "login" in request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
            
#         else:
#              # Return an 'invalid login' error message.
#             return render(request,'login.html')

def login(request):
    form_register = SignUpForm()
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            else:
#              # Return an 'invalid login' error message.
                return render(request,'login.html')
        if 'register' in request.POST:
            form_register =SignUpForm(request.POST)
            if form_register.is_valid():
                 
                form_register.save()
                username = form_register.cleaned_data.get('username')
                raw_password = form_register.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                
    context = {
        'form_register': form_register,
       
    }
    return render(request, 'login.html', context=context)
def signup(request):
    form_register = SignUpForm()
    if request.method == 'POST':
        form_register =SignUpForm(request.POST)
        if form_register.is_valid():
                 
                form_register.save()
                username = form_register.cleaned_data.get('username')
                raw_password = form_register.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
    context = {
        'form_register': form_register,
       
    }
    return render(request, 'signup.html', context=context)


        
    # context={
    #     "form_register":form_register,
    #     'luck2':request
    #    #You can ignore this if you dont use it
    #     }
    # return render(request, "login.html", context)

      
    
    
   
    
    

      
    
    


        
