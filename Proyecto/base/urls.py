from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('createacount', views.createacount, name="createacount"),
    path('cambiarcontraseña', views.cambiarcontraseña, name="cambiarcontraseña"),
    path('config/', views.config, name="config"),

]