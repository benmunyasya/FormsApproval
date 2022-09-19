from django import forms
from django.utils import timezone

from .models import New_User_Sunsystem_Process
class DateInput(forms.DateInput):
    input_type = 'date'

class NewUserSunsystemForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super(NewUserSunsystemForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = New_User_Sunsystem_Process
        fields=['User_Name','Initials','est_no','department','Surname',
        'section','Station_Park','Unit_Head_Name','Unit_Head_Title','Unit_Head_Email', 'HOD_name', 'HOD_approve', 'HOD_email',    
             'Checked_by', 'Created','Expiry','Expiry_Date']
        widgets = {
            'Expiry_Date': DateInput(),
            
            
            

            
        }
 

   
   
        
       