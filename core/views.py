from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect


# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def dashboard(request):
    user=request.user
    return render(request,'dashboard_home.html',{'user':user})

       