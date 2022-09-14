from django.urls import path,include
from viewflow.flow.viewset import FlowViewSet
from .flows import RMS_ApplicationFlow


from accounts.models import User

from .views import landing,dashboard
rmsapply_urls = FlowViewSet(RMS_ApplicationFlow).urls

app_name='access'
urlpatterns = [
    
      
   
     path('',include(rmsapply_urls),name='rms-forms'),
     
]

