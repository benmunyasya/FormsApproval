from django.urls import path,include
from viewflow.flow.viewset import FlowViewSet
from .flows import NewUserSunsystemFlow


from accounts.models import User


newusersunsystemapply_urls = FlowViewSet(NewUserSunsystemFlow).urls

app_name='newusersunsystem'
urlpatterns = [
    
      
   
     path('',include(newusersunsystemapply_urls),name='newusersunsystem'),
     
]

