from django import forms
from django.utils import timezone

from .models import Email_Request_Process
class DateInput(forms.DateInput):
    input_type = 'date'

class EmailRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmailRequestForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Email_Request_Process
        fields=['Nature_of_Request','full_name','designation','est_no','department','date_of_service_request',
        'reasons_for_request', 'HOD_name', 'HOD_approve', 'HOD_email',    
             'IT_Authority_name', 'IT_Approve','ITAuthority_email','email_assigned']
        widgets = {
            'date_of_service_request': DateInput(),
            
            
            

            
        }
   
        
       