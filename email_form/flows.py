from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator

from viewflow import  flow, lock
from viewflow.activation import STATUS
from viewflow.base import Flow, this
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from accounts.models import User
from .models import Email_Request_Process
from  django.urls import reverse_lazy
from .forms import EmailRequestForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from  django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
class EmailRequestFlow(Flow):
    process_class = Email_Request_Process
   
    
    email_start = (
        flow.Start(
           
            CreateProcessView,
            form_class= EmailRequestForm,
            task_title="Requested By:"

        ).Permission(
            auto_create=True
        ).Next(this.approve_by_HOD)
    )
    
    

    approve_by_HOD = flow.View(
        UpdateProcessView,
        task_title="APPROVAL BY HEAD OF DEPARTMENT",
        form_class=EmailRequestForm,
        
       
       
     
       
        task_result_summary="Request is {{ process.HOD_approve|yesno:'Approved,Rejected' }} by HOD ",
    
    
       
     ).Assign(
         lambda act : User.objects.filter(is_Department_Head_Authority=True ,department=act.process.department).order_by('?')[0]
    ).Next(this.confirmed) 
  
    

    confirmed = (
       
        flow.If(lambda activation: activation.process.HOD_approve)
        .Then(this.approve_by_ICT)
        .Else(this.end)
    )
    approve_by_ICT = flow.View(
        UpdateProcessView,
      
        task_title="APPROVAL BY IT DEPARTMENT",
        form_class=EmailRequestForm,
       
       
       
       
        task_result_summary="Request is {{ process.IT_Approve|yesno:'Approved,Rejected' }} by IT Authority",
        
    ).Assign(
        lambda act: User.objects.get(is_ICT_Authority=True,username='munyasya',)
        ).Next(this.system_verify)
    system_verify = (
        flow.If(lambda activation: activation.process.IT_Approve)
        

       
        .Then(this.Email_Send)
        .Else(this.end)
    )
    Email_Send = (
        flow.Handler(
            this.print_done
        ).Next(this.end)
    )

    end = flow.End()
    def print_done(self,activation):
        print('hello')