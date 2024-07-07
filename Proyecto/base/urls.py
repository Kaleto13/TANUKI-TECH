from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.home, name="home"),
    path('createacount', views.createacount, name="createacount"),
    path('cambiarcontraseña', views.cambiarcontraseña, name="cambiarcontraseña"),
    path('config/', views.config, name="config"),\
    path('setup/', views.setup_user_data, name='setup_user_data'),
    path('success/', views.success_page, name='success_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Add this line
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Add this line
    
    path('delete-account/', views.delete_account, name='delete_account'),
    path('schedule-deletion/', views.schedule_deletion, name='schedule_deletion'),
    path('profile/', views.profile, name='profile'),
]