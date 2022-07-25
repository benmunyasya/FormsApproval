from django.urls import path



from .views  import login_page,login
app_name='accounts'
urlpatterns = [
     path('login/',login_page ),
     #path('login_auth/',login,name='login' ),
     
]