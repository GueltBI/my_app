from django.urls import  path 

from . import views

urlpatterns = [

    path('/base',views.home, name = 'home'),
    path('/comissão',views.home1, name = 'home1'),
    path('/captação',views.home2, name = 'home2'),
    path('/ROA',views.home3, name = 'home3'),
    path('/alocacao',views.home4, name = 'home4'),

]
