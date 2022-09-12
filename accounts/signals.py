from django.db.models.signals import post_save,pre_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.dispatch import receiver
from accounts.models import Profile

User = get_user_model()

users = User.objects.all()


# @receiver(pre_save, sender=User)
# def assign_permissions(sender, instance, **kwargs):
       
#         if instance: 
#                   if  instance.email == 'bernard@kws.go.ke' and instance.last_name == 'Omware' and instance.first_name == 'Bernard':
#                             instance.is_ICT_Authority =  True
            
#                   if  instance.username == 'bngovi' and instance.email=='bngovi@kws.go.ke' and  instance.last_name == 'Ngovi' and instance.first_name == 'Ben':
#                             instance.is_staff==True
        

           

        
        
        

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    
    if created:
      
           
      
        Profile.objects.create(user=instance)
        if  instance.email=='bernard@kws.go.ke' and instance.last_name=='Omware' and instance.first_name=='Bernard':
          
            user=User.objects.get(username='bernard',password=instance.password)
            user.is_ICT_Authority=True
            user.save()
            g = Group.objects.get(name='Regular User')
            g.user_set.add(user)
          
        
            
       
        if  instance.email=='bngovi@kws.go.ke' and  instance.last_name=='Ngovi' and instance.first_name=='Ben':
            user=User.objects.get(username='bngovi',password=instance.password)
            user.is_staff=True
            user.save()
        else: 
            g = Group.objects.get(name='Regular User')
            g.user_set.add(instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
