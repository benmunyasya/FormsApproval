from django.db import models

from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    department = models.CharField(max_length=100,null=True,blank=True)
    is_ICT_Authority = models.BooleanField(default=False)
    is_Department_Head_Authority = models.BooleanField(default=False)
    is_kwsstaff=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}|{self.department}"