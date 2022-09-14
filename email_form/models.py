from django.db import models

# Create your models here.
from msilib.schema import Signature


from viewflow.models import Process

from datetime import datetime
from access.models import DEPARTMENTS,EMAIL_REQUEST_TYPE_CHOICES
from accounts.models import User
from multiselectfield import MultiSelectField

class Email_Request_Process(Process):
    """ Personal Details"""
    Nature_of_Request = models.CharField(choices=EMAIL_REQUEST_TYPE_CHOICES,max_length=30)
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=30)
    est_no = models.CharField(max_length=30)
    department=models.CharField(max_length=30,choices=DEPARTMENTS)
    date_of_service_request = models.DateField()
    reasons_for_request=models.TextField(null=True,blank=True,help_text='State your reasons for requesting an email')
    #approval by hod
    HOD_name = models.CharField(max_length=50,null=True,blank=True)
    HOD_approve=models.BooleanField(default=False,null=True,blank=True)
    date_approved_by_department_head=models.DateField(auto_now=True,null=True,blank=True)
    HOD_email = models.EmailField(null=True,blank=True,help_text='Enter Your email to digitally sign . i.e ben@kws.go.ke')
    #approval by IT
    IT_Authority_name = models.CharField(max_length=30,null=True,blank=True)
    IT_Approve=models.BooleanField(default=False,null=True,blank=True)
    date_approved_by_it=models.DateField(auto_now=True,null=True)
    ITAuthority_email = models.EmailField(null=True,blank=True,help_text='Enter Your email to digitally sign . i.e ben@kws.go.ke')
    IT_Remarks=models.TextField(null=True,blank=True,help_text='You can leave blank if no comments')
    
    email_assigned= models.EmailField(null=True,blank=True,help_text='Enter the  email that you have assigned to the applicant ')
    date_email_address_created=models.DateField(auto_now=True,null=True)
    fully_approved=models.BooleanField(default=False,null=True,blank=True)
   
