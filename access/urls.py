from django.urls import path,include
from viewflow.flow.viewset import FlowViewSet
from .flows import RMS_ApplicationFlow


from accounts.models import User
from accounts.views import login_page
from .views import landing,dashboard
rmsapply_urls = FlowViewSet(RMS_ApplicationFlow).urls
app_name='access'
urlpatterns = [
     path('',landing,name='landing'),
     path('login',login_page ,name='login'),
      
     path('dashboard',dashboard,name='dashboard'),
     path('request_forms/',include(rmsapply_urls),name='request-forms'),
]

