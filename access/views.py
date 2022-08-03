from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request,'landing.html')
@login_required(login_url='/accounts/login/')
def dashboard(request):
    user=request.user
    if user.is_kwsstaff:

         
         return HttpResponseRedirect('/request_forms/')
    else:
        return HttpResponseRedirect('/request_forms/tasks/')