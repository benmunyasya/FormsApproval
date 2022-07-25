from django.utils.decorators import method_decorator

from viewflow import  flow, lock
from viewflow.activation import STATUS
from viewflow.base import Flow, this
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from accounts.models import User
from . import models, views, forms
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from  django.urls import reverse_lazy
class RMSProcessCreate(CreateView):
    
    model=models.RMSGeneralInformationProcess
    template_name='rms_start.html'
    success_url=reverse_lazy('dashboard')
    form_class=forms.GeneralInformationForm
   
    
    def form_valid(self,form):
        return super(RMSProcessCreate,self).form_valid(form)  

class RMS_ApplicationFlow(Flow):
    process_class = models.RMSGeneralInformationProcess
    
    start = (
        flow.Start(
            CreateProcessView,
              
              
             fields=['request_type', 'last','first','middle','salutation','user_type','temporary_staff','est_no','email','mobile_no',
         'company_name','job_title','department','station','section','area','date'],
        task_title="General Infomation"
        ).Permission(
            auto_create=True
        ).Next(this.approve_by_HOD)
    )
    
    

    approve_by_HOD = flow.View(
        UpdateProcessView,
         task_title="Head Department Approval",
        fields=['HOD_name', 'HOD_approve', 'HOD_email'],
       task_result_summary="Request is {{ process.HOD_approve|yesno:'Approved,Rejected' }} by HOD "
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
        fields=['ICT_Authority_name', 'ICT_Approve','ICTAuthority_email'],
        
        task_result_summary="Request is {{ process.ICT_Approve|yesno:'Approved,Rejected' }} by ICT Authority "
    ).Assign(
        lambda act: User.objects.get(is_ICT_Authority=True)
        ).Next(this.check_approve_by_ICT)
    check_approve_by_ICT = (
        flow.If(lambda activation: activation.process.ICT_Approve)
        .Then(this.send)
        .Else(this.end)
    )
    send = (
        flow.Handler(
            this.send_hello_world_request
        ).Next(this.end)
    )

    end = flow.End()
    def send_hello_world_request(self, activation):
        print('approved download  and print your form')

           
            
            
            
            