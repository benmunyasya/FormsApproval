from django.urls import path,include
from viewflow.flow.viewset import FlowViewSet
from .flows import RMS_ApplicationFlow,EmailRequestFlow


from accounts.models import User

from .views import landing,dashboard
rmsapply_urls = FlowViewSet(RMS_ApplicationFlow).urls
emailapply_urls = FlowViewSet(EmailRequestFlow).urls
app_name='access'
urlpatterns = [
     path('',landing,name='landing'),
    
      
     path('dashboard',dashboard,name='dashboard'),
     path('forms/',include(rmsapply_urls),name='RMS'),
     path('forms/',include(emailapply_urls),name='EMAIL'),
]

