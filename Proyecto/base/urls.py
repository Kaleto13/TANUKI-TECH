from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('createacount', views.createacount, name="createacount")
]