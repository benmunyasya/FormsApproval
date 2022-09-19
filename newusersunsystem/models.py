from django.db import models

# Create your models here.



from viewflow.models import Process

from datetime import datetime
from access.models import DEPARTMENTS
from accounts.models import User
from multiselectfield import MultiSelectField

class New_User_Sunsystem_Process(Process):
    """ Personal Details"""
    
    User_Name = models.CharField(max_length=100)
    Initials = models.CharField(max_length=100,help_text='Must be 3 letters')
    est_no = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    department=models.CharField(max_length=100,choices=DEPARTMENTS)
    section=models.CharField(max_length=100)
    Station_Park =models.CharField(max_length=100)
    
    #To be filled by unit head
    Unit_Head_Name = models.CharField(max_length=50,null=True,blank=True)
    Unit_Head_Title =models.CharField(max_length=50,null=True,blank=True)
    Unit_Head_Email = models.EmailField(null=True,blank=True,help_text='Enter Your email to digitally sign . i.e ben@kws.go.ke')
    date_approved_by_Unit_head=models.DateField(auto_now=True,null=True,blank=True)

    HOD_email = models.EmailField(null=True,blank=True,help_text='Enter Your email to digitally sign . i.e ben@kws.go.ke')
    HOD_name = models.CharField(max_length=50,null=True,blank=True)
    HOD_approve=models.BooleanField(default=False,null=True,blank=True)
    date_approved_by_department_head=models.DateField(auto_now=True,null=True,blank=True)
   
    #approval by IT
    Checked_by= models.CharField(max_length=30,null=True,blank=True)
    Created=models.BooleanField(default=False,null=True,blank=True)
    date_created=models.DateField(auto_now=True,null=True)
    Expiry=models.BooleanField(default=False,null=True,blank=True)
    Expiry_Date=models.DateField(null=True,blank=True)
   
   
   
