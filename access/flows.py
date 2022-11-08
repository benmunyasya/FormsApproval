
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from viewflow import  flow, lock
from viewflow.activation import STATUS
from viewflow.base import Flow, this
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from accounts.models import User
from .models import  RMSGeneralInformationProcess
from  django.urls import reverse_lazy
from .forms import RMSForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from  django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

from .views import start_RMSGeneralInformationProcess,HodApprovalView


class RMS_ApplicationFlow(Flow):
    process_class = RMSGeneralInformationProcess
    
    rms_start = (
        flow.Start(
           
            CreateProcessView,
            
            form_class=RMSForm,
  initial={
      
        #'first':super(CreateView),
        # "Full_Name":lambda act: act.request.user.first_na''me + act.request.user.last_name,
        #  "Signature":lambda act: act.request.user.email,
       
    },
         task_title="General Infomation"
        ).Permission(
         auto_create=True
        ).Next(this.approve_by_HOD)
    )
    
    

    approve_by_HOD = flow.View(
       
      
        UpdateProcessView,
        task_title="Department Head AUTHORIZATION",
    
       
       
         form_class=RMSForm,
       initial={
        "HOD_name" : "Kennedy Otieno",
        "HOD_email" : "kotieno@kws.go.ke",
       
    },

        task_result_summary="Request is {{ process.HOD_approve|yesno:'Approved,Rejected' }} by HOD ",
  
     ).Permission(auto_create=True
     ).Next(this.confirmed) 
  
     
     
   
    confirmed = (
       
        flow.If(lambda activation: activation.process.HOD_approve)
        .Then(this.approve_by_ICT)
        .Else(this.end)
    )
    approve_by_ICT = flow.View(
        UpdateProcessView,
       # ICT_Authority_name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
        task_title="ICT APPROVING AUTHORITY/DATA OWNER",
        
        form_class=RMSForm,
        initial={
        "ICT_Authority_name" : "Bernard Omware",
        "ICTAuthority_email" : "bernard@kws.go.ke",
       
    },
         
        

       # success_url = '/request_form/tasks',
       
       # fields=['ICT_Authority_name', 'ICT_Approve','ICTAuthority_email'],
       
        task_result_summary="Request is {{ process.ICT_Approve|yesno:'Approved,Rejected' }} by ICT Authority ",
        
    ).Assign(
        lambda act: User.objects.get(is_ICT_Authority=True)
        ).Next(this.system_verify)
    system_verify = (
        flow.If(lambda activation: activation.process.ICT_Approve)
        

       
        .Then(this.Email_Send)
        .Else(this.end)
    )
    Email_Send = (
        flow.Handler(
            this.send_form_complete_email
        ).Next(this.end)
    )

    end = flow.End()
   
    def send_form_complete_email(self, activation):
           if activation.process.ICT_Approve == True :
                current_process=RMSGeneralInformationProcess.objects.get(process_ptr_id=activation.process.id)
                current_process.fully_approved=True
                current_process.save()
           print(f'{activation.process} finished')
        # subject = activation.process
        # message = 'Hi {user.username}, thank you for registering in geeksforgeeks.'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['benngovi47@gmail.com' ]
        # send_mail( subject, message, email_from, recipient_list )

     
            
          
            
            