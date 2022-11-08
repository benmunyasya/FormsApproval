from viewflow.models import Task,Process
from access.flows import RMS_ApplicationFlow
from access.models import RMSGeneralInformationProcess
from email_form.models import Email_Request_Process
from email_form.flows import EmailRequestFlow
from newusersunsystem.flows import NewUserSunsystemFlow

def tasks_counts(request):
    if request.user.is_authenticated:
        return {
          
            'inbox_count': Task.objects.inbox([RMS_ApplicationFlow],request.user).count() +
                     Task.objects.inbox([EmailRequestFlow],request.user).count()+
                             Task.objects.inbox([NewUserSunsystemFlow],request.user).count(),
           
            'active_workflows':Process.objects.filter_available([RMS_ApplicationFlow,EmailRequestFlow],request.user).filter(finished__isnull=True),
             'active_workflows_count':Process.objects.filter_available([RMS_ApplicationFlow,EmailRequestFlow],request.user).filter(finished__isnull=True).count(),
             'finished_workflows':Process.objects.filter_available([RMS_ApplicationFlow,EmailRequestFlow],request.user).filter(finished__isnull=False),
          
           'finished_workflows_count':Process.objects.filter_available([RMS_ApplicationFlow,EmailRequestFlow],request.user).filter(finished__isnull=False).count(),
           'pending_hod_approval_count':RMSGeneralInformationProcess.objects.filter(HOD_approve=False).count()+
                                        Email_Request_Process.objects.filter(HOD_approve=False).count()          ,
            'rms_inbox_count': Task.objects.inbox([RMS_ApplicationFlow],request.user).count() ,
            'email_inbox_count': Task.objects.inbox([EmailRequestFlow],request.user).count() ,
            'new_user_sunsystem_inbox_count': Task.objects.inbox([NewUserSunsystemFlow],request.user).count() ,
            'queue_count': Task.objects.queue([RMS_ApplicationFlow], request.user).count(),
           
           
    }
    return {}
def resolver_context_processor(request):
    return {
        
        'app_name': request.resolver_match.app_name,
        'namespace': request.resolver_match.namespace,
        'url_name': request.resolver_match.url_name,
        'process_list_url':'{}/{}/'
    }
  