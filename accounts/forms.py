from  .models import User
from django import forms
from allauth.account.forms import SignupForm



from django import forms


class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm,self).__init__(*args, **kwargs)
        self.fields['est_no']=forms.CharField(required=True)
        self.fields['area']=forms.CharField(required=True)
        self.fields['department']=forms.CharField(required=True)
     
               
    
 


    def save(self,request):
        est_no=self.cleaned_data.pop('est_no')
        area=self.cleaned_data.pop('area')
        department=self.cleaned_data.pop('department')
        
        user=super(CustomSignUpForm,self).save(request)
        user.is_kwsstaff=True
        user.is_superuser=True
        user.est_no=est_no
        user.area=area
        user.department=department
        user.save()
        return user

        
       