from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,'login.html')
from django.contrib.auth import authenticate, login

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'landing.html')
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        return render(request,'login.html')