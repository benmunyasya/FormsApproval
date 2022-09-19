from django.db import models
from accounts.models import User
# Create your models here.
class UserNotifications(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_id}"
    
    class Meta:
        verbose_name = "Notifications"
        verbose_name_plural = verbose_name