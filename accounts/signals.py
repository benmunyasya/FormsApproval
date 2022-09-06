from django.db.models.signals import post_save,pre_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.dispatch import receiver
from accounts.models import Profile

User = get_user_model()

users = User.objects.all()


@receiver(pre_save, sender=User)
def assign_permissions(sender, instance, **kwargs):
        g = Group.objects.get(name='Regular User')
    
        if  instance.email == 'bernard@kws.go.ke' and instance.last_name == 'Omware' and instance.first_name == 'Bernard':
            instance.is_ICT_Authority =  True
            instance.is_kwsstaff=False
        if  instance.username == 'bngovi' and instance.email=='bngovi@kws.go.ke' and  instance.last_name == 'Ngovi' and instance.first_name == 'Ben':
            instance.is_staff=True
        else:
            g.user_set.add(instance)
            instance.is_kwsstaff=True
           

        
        
        

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    
    if created:
        if  instance.email=='bernard@kws.go.ke' and instance.last_name=='Omware' and instance.first_name=='Bernard':
            instance.is_ICT_Authority =  True
            instance.is_kwsstaff=False
        if  instance.email=='bngovi@kws.go.ke' and  instance.last_name=='Ngovi' and instance.first_name=='Ben':
            instance.is_staff=True
           

        instance.is_superuser=True
        instance.is_kwsstaff=True
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
