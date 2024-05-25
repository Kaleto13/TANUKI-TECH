from django.urls import path
from . import views

urlpatterns=[
    path('prueba', views.home, name="home"),
]