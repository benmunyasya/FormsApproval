from viewflow import  flow, lock
from viewflow.activation import STATUS
from viewflow.base import Flow, this
from viewflow.decorators import flow_start_view
from .forms import RMSForm
from .models import RMSGeneralInformationProcess
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from viewflow.flow.views.utils import get_next_task_url
def send_workflow_created_notification(request):
       send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False
     )


@flow_start_view
def start_RMSGeneralInformationProcess(request, **kwargs):
    request.activation.prepare(request.POST or None, user=request.user)
    form = RMSForm(request.POST or None)

    if form.is_valid():
        form.save()
        send_mail(
         "RMS ACCOUNT REQUISITION"  ,
          'A work flow that needs your attention was just created',
         'bngovi@kws.go.ke',
          ['kotieno@kws.go.ke'],
        )
       
        request.activation.done()

        return redirect(get_next_task_url(request, request.activation.process))

    return render(request, 'rms_start.html',{
        'form': form,
        'activation':request.activation
    })

