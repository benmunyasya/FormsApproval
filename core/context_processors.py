from viewflow.models import Task,Process
from access.flows import RMS_ApplicationFlow
from email_form.flows import EmailRequestFlow

def tasks_counts(request):
    if request.user.is_authenticated:
        return {
          
            'inbox_count': Task.objects.inbox([RMS_ApplicationFlow],request.user).count() + Task.objects.inbox([EmailRequestFlow],request.user).count(),
            'rms_inbox_count': Task.objects.inbox([RMS_ApplicationFlow],request.user).count() ,
            'email_inbox_count': Task.objects.inbox([EmailRequestFlow],request.user).count() ,
            'queue_count': Task.objects.queue([RMS_ApplicationFlow], request.user).count()
           
    }
    return {}
