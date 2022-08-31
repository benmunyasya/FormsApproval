from django.urls import path,include
from viewflow.flow.viewset import FlowViewSet
from .flows import RMS_ApplicationFlow,EmailRequestFlow


from accounts.models import User
from accounts.views import login_page
from .views import landing,dashboard
rmsapply_urls = FlowViewSet(RMS_ApplicationFlow).urls
#emailapply_urls = FlowViewSet(EmailRequestFlow).urls
app_name='access'
urlpatterns = [
     path('',landing,name='landing'),
     path('login',login_page ,name='login'),
      
     path('dashboard',dashboard,name='dashboard'),
     path('rms_forms/',include(rmsapply_urls),name='rms-forms'),
     #path('emailforms/',include(emailapply_urls),name='emailforms'),
]

