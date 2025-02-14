from msilib.schema import Signature
from django.db import models

# Create your models here.
from django.db import models

from core.models import CONSERVATION_AREAS,STATIONS


from viewflow.models import Process

from datetime import datetime

from accounts.models import User
from multiselectfield import MultiSelectField

ACCESS_AND_MULTIPLE_GROUP_SELECTION_CHOICES=((('Systems Administrator','Senior Management')),(('Finance Mananger','Finance Excutive')))
REQUEST_TYPE_CHOICES=(('New User Account', 'New User Account'), ('Modify Access Permission', 'Modify Access Permission'), ('Update Contact Information', 'Update Contact Information'))
DEPARTMENTS=(('ICT', 'ICT'),('Customer Service', 'Customer Service'), ('Finance', 'Finance'),('Parks & Reserves', 'Parks & Reserves'),('Marketing', 'Marketing'),('Internal Audit', 'Internal Audit'),('Revenue Protection Unit', 'Revenue Protection Unit'))
EMAIL_REQUEST_TYPE_CHOICES=(('INDIVIDUAL', 'INDIVIDUAL'), ('EMAIL DISTRIBUTION LIST', 'EMAIL DISTRIBUTION LIST'))
class RMSGeneralInformationProcess(Process):
    
    request_type = models.CharField(choices=REQUEST_TYPE_CHOICES,max_length=30)
    """ Personal Details """
    last = models.CharField(max_length=30)
    first = models.CharField(max_length=30)
    middle = models.CharField(max_length=30)
    salutation = models.CharField(max_length=30)
    
    
    user_type = models.CharField(choices=(('RMS Manager/Approver', 'RMS Manager/Approver'), ('User', 'User')),default='User',max_length=30)
    temporary_staff=models.CharField(choices=(('Yes', 'Yes'), ('No', 'No')),max_length=30,default='No')

    est_no = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    job_title=models.CharField(max_length=30)
    department=models.CharField(max_length=30,choices=DEPARTMENTS)
    station=MultiSelectField(max_length=100,choices=STATIONS)
    section=models.CharField(max_length=30)
    area=models.CharField(max_length=100,choices=CONSERVATION_AREAS)
    date = models.DateField(null=True)
    #access  groups

    ICT= MultiSelectField(null=True,blank=True,choices=(('Systems Administrator', 'Systems Administrator'), ('Senior Management', 'Senior Management')),max_length=50)
    FINANCE= MultiSelectField(null=True,blank=True,choices=(('Finance Mananger', 'Finance Mananger'), ('Finance Executive', 'Finance Executive')),max_length=50)
    CUSTOMER_SERVICE= MultiSelectField(null=True,blank=True,choices=(('Customer Service Officers', 'Customer Service Officers'), ('Customer Service Users', 'Customer Service Users'),('Checker', 'Checker'),('Entry Clerk', 'Entry Clerk'),('Purchase Clerk', 'Purchase Clerk'),('Usher', 'Usher')),max_length=50)
    MARKETING= MultiSelectField(null=True,blank=True,choices=(('Marketing Officers', 'Marketing Officers'), ('Marketing Executive', 'Marketing Executive')),max_length=50)
    PARKS_AND_RESERVES= MultiSelectField(null=True,blank=True,choices=(('Ranger', 'Ranger'), ('Park Management', 'Park Management')),max_length=50)
    REVENUE_PROTECTION_UNIT= models.CharField(null=True,blank=True,choices=(('RPU', 'RPU'),('None', 'None')), default='None',max_length=50)
    INTERNAL_AUDIT= models.CharField(null=True,blank=True,choices=(('Internal Auditor', 'Internal Auditor'),('None', 'None')),default='None',max_length=50)
    date_submitted=models.DateField(default=datetime.now,null=True,blank=True)
    date_completed=models.DateField(default=datetime.now,null=True,blank=True)
    
    ## USER ACCOUNT REQUEST
    Full_Name=models.CharField(max_length=100)
    Signature=models.EmailField(help_text='Enter Your email to digitally sign . i.e ben@kws.go.ke')
    Date = models.DateField(null=True)
    #ict verification
    ICT_Authority_name = models.CharField(max_length=30,null=True,blank=True)
    ICT_Approve=models.BooleanField(default=False,null=True,blank=True)
    date_approved_by_ict=models.DateField(auto_now=True,null=True)
    ICTAuthority_email = models.EmailField(null=True,blank=True,help_text='Enter Your email to digitally sign . i.e ben@kws.go.ke')
    ICT_Remarks=models.TextField(null=True,blank=True,help_text='You can leave blank if no comments')
    #Head department verification
    HOD_name = models.CharField(max_length=50,null=True,blank=True)
    HOD_approve=models.BooleanField(default=False,null=True,blank=True)
    date_approved_by_department_head=models.DateField(auto_now=True,null=True,blank=True)
    HOD_email = models.EmailField(null=True,blank=True,help_text='Enter Your email to digitally sign . i.e ben@kws.go.ke')
    HOD_Remarks=models.TextField(null=True,blank=True,help_text='You can leave blank if no comments')
    fully_approved=models.BooleanField(default=False,null=True,blank=True)
