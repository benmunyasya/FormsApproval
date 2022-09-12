from django import forms
from django.utils import timezone

from .models import Email_Request_Process, RMSGeneralInformationProcess
class DateInput(forms.DateInput):
    input_type = 'date'
class RMSForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RMSForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = RMSGeneralInformationProcess
        fields=['request_type', 'last','first','middle','salutation','user_type','temporary_staff','est_no','email','mobile_no',
         'company_name','job_title','department','station','section','area','date','ICT','FINANCE','CUSTOMER_SERVICE',
         'MARKETING','PARKS_AND_RESERVES','REVENUE_PROTECTION_UNIT','INTERNAL_AUDIT' ,'Full_Name','Signature','Date',
         'HOD_name', 'HOD_approve', 'HOD_email','HOD_Remarks',
         'ICT_Authority_name', 'ICT_Approve','ICTAuthority_email','ICT_Remarks']
        widgets = {
            'date': DateInput(),
            'Date':DateInput(),
            'user_type':forms.RadioSelect(),
            'temporary_staff':forms.RadioSelect(),
            'REVENUE_PROTECTION_UNIT':forms.RadioSelect(),
            'INTERNAL_AUDIT':forms.RadioSelect(),
           

            
        }
class EmailRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmailRequestForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Email_Request_Process
        fields=['Nature_of_Request','full_name','designation','est_no','department','date_of_service_request','reasons_for_request']
        widgets = {
            'date_of_service_request': DateInput(),
            
            
            

            
        }
   
        
       