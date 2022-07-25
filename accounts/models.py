from django.db import models


from django.db import models




from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    is_verified = models.BooleanField(default=False)
    is_ICT_Authority = models.BooleanField(default=False)
    is_Department_Head_Authority = models.BooleanField(default=False)
    is_kwsstaff=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} | {self.first_name} {self.last_name}"