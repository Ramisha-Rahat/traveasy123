from django.urls import path
from django.contrib.auth import views as auth_views
from registration.views import *


urlpatterns = [
   path('accounts/login/',login_page , name="login" ),
   path('register/' , register_page , name="register"),
   path('logout/', UserLogout, name="logout"),
   path('login/<email_token>/' , activate_email , name="activate_email"),
]
