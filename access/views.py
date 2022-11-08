from tkinter import E
from viewflow import  flow, lock
from viewflow.activation import STATUS
from viewflow.base import Flow, this
from WORKFLOW.settings import EMAIL_HOST_USER
from viewflow.decorators import flow_start_view,flow_view
from viewflow.flow.views import StartFlowMixin, FlowMixin,UpdateProcessView
from .forms import RMSForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import RMSGeneralInformationProcess
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from viewflow.flow.views.utils import get_next_task_url
from django.urls import reverse_lazy
from django.db import transaction
def send_workflow_created_notification(request):
       send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False
     )



def start_RMSGeneralInformationProcess(request, **kwargs):
    request.activation.prepare(request.POST or None, user=request.user)
    form = RMSForm(request.POST or None,initial={
        "first" : request.user.first_name,
        "last" : request.user.last_name,
        "Full_Name":request.user.first_name +  request.user.last_name,
         "Signature":request.user.email,
       
    })
   

    if form.is_valid():
        rmsform=form.save()
        send_mail(
        'RMS WORKFLOW',
       'RMS WORKFLOW HAS BEEN CREATED AND STARTED.Open http://virtual.kws.local to check',
 EMAIL_HOST_USER,
    ['bngovi@kws.local'],
    fail_silently=True
     )
       
        request.activation.process.rmsform = rmsform
        request.activation.done()

        return redirect(get_next_task_url(request, request.activation.process))

    return render(request, 'rms_start.html',{
        'form': form,
        'activation':request.activation
    })


class HodApprovalView(UpdateProcessView):
    
    form_class = RMSForm
    model = RMSGeneralInformationProcess
    initial={
        " HOD_name" : "Kennedy Otieno",
        "HOD_email" : "kotieno@kws.go.ke",
       
    }

    def get_success_url(self):
        success_url='viewflow/flow/process_detail.html'
        return redirect(success_url)

    def get_object(self, queryset=None):
        """Return the process for the task activation."""
        return self.activation.process

    def form_valid(self, form):
        form.save()

        

        if '_continue' in form.data:
            transaction.on_commit(self.activation_done)
        
        return super(UpdateView, self).form_valid(form)