"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app1.views import *
from app2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1_first/',app1_first,name='app1_first'),
    path('app1_second/',app1_second,name='app1_second'),
    
    path('first_app2/',first_app2,name='first_app2'),
    path('second_app2/',second_app2,name='second_app2'),
]






