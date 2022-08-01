from django.http import HttpResponse
from django.utils.decorators import method_decorator

from viewflow import  flow, lock
from viewflow.activation import STATUS
from viewflow.base import Flow, this
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from accounts.models import User
from .models import RMSGeneralInformationProcess
from  django.urls import reverse_lazy
from .forms import RMSForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from  django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class RMSProcessCreate(CreateView):
    
    model=RMSGeneralInformationProcess
    template_name='rms_start.html'
    success_url=reverse_lazy('dashboard')
   
   
    
    def form_valid(self,form):
        return super(RMSProcessCreate,self).form_valid(form)


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
         task_title="Head Department Approval",
        form_class=RMSForm,
       
      #  fields=['HOD_name', 'HOD_approve', 'HOD_email'],
       
        task_result_summary="Request is {{ process.HOD_approve|yesno:'Approved,Rejected' }} by HOD ",
       
       
    ).Assign(
        lambda act: User.objects.filter(is_Department_Head_Authority=True).order_by('?')[0]
    ).Next(this.check_approve_HOD) 
  
    

    check_approve_HOD = (
       
        flow.If(lambda activation: activation.process.HOD_approve)
        .Then(this.approve_by_ICT)
        .Else(this.end)
    )
    approve_by_ICT = flow.View(
        UpdateProcessView,
        task_title="ICT Authority Approval",
        form_class=RMSForm,
      
       # fields=['ICT_Authority_name', 'ICT_Approve','ICTAuthority_email'],
       
        task_result_summary="Request is {{ process.ICT_Approve|yesno:'Approved,Rejected' }} by ICT Authority ",
        success_url=reverse_lazy('tasks')
    ).Assign(
        lambda act: User.objects.get(is_ICT_Authority=True)
        ).Next(this.check_approve_by_ICT)
    check_approve_by_ICT = (
        flow.If(lambda activation: activation.process.ICT_Approve)
       
        .Then(this.Email_Send)
        .Else(this.end)
    )
    Email_Send = (
        flow.Handler(
            this.send_hello_world_request
        ).Next(this.end)
    )

    end = flow.End()
    def send_hello_world_request(self, activation):
        print('approved download  and print your form')

           
            
            
            
            