from django.urls import path,include
from viewflow.flow.viewset import FlowViewSet
from .flows import EmailRequestFlow


from accounts.models import User


emailapply_urls = FlowViewSet(EmailRequestFlow).urls

app_name='email_form'
urlpatterns = [
    
     path('',include(emailapply_urls),name='email-forms'),
     
]

