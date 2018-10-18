"""ask URL Configuration

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
from django.conf.urls import patterns, url, include


urlpatterns =                                              
   url(r'^$', 'qa.views.test'),                                                              
   url(r'^login/.*$', 'qa.views.test', name='login'),                                    
   url(r'^signup/.*', 'qa.views.test', name='signup'),                                   
   url(r'^question/(?P<id>[0-9]+)/$', 'qa.views.test', name='question'),                 
   url(r'^ask/.*', 'qa.views.test', name='ask'),                                         
   url(r'^popular/.*', 'qa.views.test', name='popular'),                                 
   url(r'^new/.*', 'qa.views.test', name='new'),                                         
)   

