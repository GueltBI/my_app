from django.urls import  path 

from . import views

urlpatterns = [

    path('/base',views.home, name = 'home'),
    path('/comissão',views.home1, name = 'home1'),
    path('/captação',views.home2, name = 'home2'),
    path('/ROA',views.home3, name = 'home3'),
    path('/alocacao',views.home4, name = 'home4'),
    path('/estruturadas',views.home5, name = 'home5'),
    path('/AAI',views.home6, name = 'home6')

]
