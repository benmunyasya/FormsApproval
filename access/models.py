from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from flask_login import user_accessed, user_loaded_from_request, user_logged_in, user_login_confirmed
from sqlalchemy import ForeignKey, true
from viewflow.models import Process

from datetime import datetime

from accounts.models import User

from phonenumber_field.modelfields import PhoneNumberField
ACCESS_AND_MULTIPLE_GROUP_SELECTION_CHOICES=((('Systems Administrator','Senior Management')),(('Finance Mananger','Finance Excutive')))
REQUEST_TYPE_CHOICES=(('New User Account', 'New User Account'), ('Modify Access Permission', 'Modify Access Permission'), ('Update Contact Information', 'Update Contact Information'))


class RMSGeneralInformationProcess(Process):
    applicant=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    request_type = models.CharField(choices=REQUEST_TYPE_CHOICES,max_length=30)
    """ Personal Details """
    last = models.CharField(max_length=30)
    first = models.CharField(max_length=30)
    middle = models.CharField(max_length=30)
    salutation = models.CharField(max_length=30)
    
    
    user_type = models.CharField(choices=(('RMS Manager/Approver', 'RMS Manager/Approver'), ('User', 'User')),max_length=30)
    temporary_staff=models.CharField(choices=(('Yes', 'Yes'), ('No', 'No')),max_length=30)

    est_no = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    job_title=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    station=models.CharField(max_length=30)
    section=models.CharField(max_length=30)
    area=models.CharField(max_length=30,default='SOUTHERN')
    date = models.DateField()
 
    date_submitted=models.DateField(default=datetime.now,null=True,blank=True)
    date_completed=models.DateField(default=datetime.now,null=True,blank=True)
    #ict verification
    ICT_Authority_name = models.CharField(max_length=30,null=True,blank=True)
    ICT_Approve=models.BooleanField(default=False,null=True,blank=True)
    date_approved_by_ict=models.DateField(auto_now=True,null=True)
    ICTAuthority_email = models.EmailField(null=True,blank=True)
    
    #Head department verification
    HOD_name = models.CharField(max_length=30,null=True,blank=True)
    HOD_approve=models.BooleanField(default=False,null=True,blank=True)
    date_approved_by_department_head=models.DateField(auto_now=True,null=True,blank=True)
    HOD_email = models.EmailField(null=True,blank=True)

    
   