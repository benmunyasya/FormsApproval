from urllib import request
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
 
# Create your views here.
def logout(request):
    logout(request)
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        
        
        login(request, user)
        messages.success(request, "Login successful." )
        print(messages)
        return render(request,'landing.html')
       
       
    else:
            messages.error(request,'username or password not correct')
            return redirect('login')

class LDAPLogout(APIView):
    """
    Class for logging out a user by clearing his/her session
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        Api to logout a user
        :param request:
        :return:
        """
        logout(request)
        data={'detail': 'User logged out successfully'}
        return Response(data, status=200)