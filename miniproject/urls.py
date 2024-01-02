"""
URL configuration for miniproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import handler404

from django.contrib import admin
from django.urls import path, include
from home.views import *
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.http import HttpResponseNotFound


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name='register'),
    path('logout/', logout, name='logout'),
    path('*', lambda request: render(request, '404.html')),
    
]

