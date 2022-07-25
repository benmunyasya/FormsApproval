from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def landing(request):
    return render(request,'landing.html')
@login_required(login_url='/accounts/login/')
def dashboard(request):
    user=request.user
    
    context={'user':user}
    return render(request,'dashboard.html',context)