from django.db import models

from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    
    is_ICT_Authority = models.BooleanField(default=False)
    is_Department_Head_Authority = models.BooleanField(default=False)
   
    department = models.CharField(max_length=100,null=True,blank=True)
    area=models.CharField(max_length=100,null=True,blank=True)
    est_no=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.username}"
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
    
   

    def __str__(self):
        return f"{self.user.username}'s profile"