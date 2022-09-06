from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator

from viewflow import  flow, lock
from viewflow.activation import STATUS
from viewflow.base import Flow, this
from viewflow.flow.views import CreateProcessView, UpdateProcessView,get_next_task_url
from accounts.models import User
from .models import Email_Request_Process, RMSGeneralInformationProcess
from  django.urls import reverse_lazy
from .forms import RMSForm,EmailRequestForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from  django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail




class RMS_ApplicationFlow(Flow):
    process_class = RMSGeneralInformationProcess
    
    rms_start = (
        flow.Start(
           
            CreateProcessView,
              
              
            form_class=RMSForm,
           
         
         task_title="General Infomation"
        ).Permission(
            auto_create=True
        ).Next(this.approve_by_HOD)
    )
    
    

    approve_by_HOD = flow.View(
        UpdateProcessView,
        task_title="Department Head AUTHORIZATION",
        form_class=RMSForm,
        
       
       
     
       
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
       # ICT_Authority_name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
        task_title="ICT APPROVING AUTHORITY/DATA OWNER",
        form_class=RMSForm,
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
class EmailRequestFlow(Flow):
    process_class = Email_Request_Process
    
    email_start = (
        flow.Start(
           
            CreateProcessView,
             
              
            form_class=EmailRequestForm,
           
         
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
        lambda act: User.objects.get(username='bomware')
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
     
            
            
            
            