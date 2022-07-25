from django import forms
from django.utils import timezone

from .models import RMSGeneralInformationProcess
from .import models
class GeneralInformationForm(forms.ModelForm):
        def __init__(self):
                
                self.fields['user_type'] = forms.ChoiceField(label='User Type',choices=(('RMS Manager/Approver', 'RMS Manager/Approver'), ('User', 'User')), required=True,widget=forms.RadioSelect(attrs={ 'class': 'form-control' }))   

                class Meta:
                        model=RMSGeneralInformationProcess
                        fields=['request_type', 'last','first','middle','salutation','user_type','temporary_staff','est_no','email','mobile_no',
                              'company_name','job_title','department','station','section','area','date']
        

        
        
       