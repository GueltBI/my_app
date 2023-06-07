"""
URL configuration for main project.

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
from django.contrib import admin
from django.urls import path
from django.urls import include
from mainn import views

urlpatterns = [
    
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('comissão/',views.home1, name='home1'),
    path('captação/',views.home2, name='home2'),
    path('ROA/',views.home3, name = 'home3'),
    path('alocacao/',views.home4, name = 'home4'),
    path('estruturadas/',views.home5, name = 'home5'),


]
