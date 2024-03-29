"""aptim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from users.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from core.views import IndexTemplateView
# One step view = we can skip email verification for now
# django registration documentation to do email verifcation sysytem TODO
urlpatterns = [
    path('admin/', admin.site.urls),

     #path to djoser end points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
	
	#path to our account's app endpoints
    path("api/accounts/",include("users.api.urls")),
    # path("accounts/register",
    #      RegistrationView.as_view(
    #          form_class=CustomUserForm,
    #          success_url="/",
    #      ), name="django_registration_register"),

#     path("accounts/",
#          include("django_registration.backends.one_step.urls")),

#     # login url by django
#     path("accounts/",
#          include("django.contrib.auth.urls")),

#     # login via browser
#     path("api-auth/",
#          include("rest_framework.urls")),

    path("api/",
         include("users.api.urls")),

#     # login end points via rest
#     path("api/rest-auth/",
#          include("rest_auth.urls")),

#     # register end points via rest
#     path("api/rest-auth/registration/",
#          include("rest_auth.registration.urls")),
    
    # path(r'^auth/obtain_token/', obtain_jwt_token),
     
    # path(r'^auth/refresh_token/', refresh_jwt_token),

    re_path("app/", IndexTemplateView.as_view(), name="app")
]
