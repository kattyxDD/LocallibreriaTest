
from django.urls import path 
from . import views

urlpatterns = [
    #llamada al metodo index creado
    path('', views.index,name='index'),
]