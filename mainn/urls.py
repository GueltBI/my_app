from django.urls import  path 

from . import views

urlpatterns = [

    path('/base',views.home, name = 'home'),
    path('/dados',views.home1, name = 'home1'),
    path('/dados2',views.home2, name = 'home2')


]