from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name='login'),
    path('adminka/', views.adminMenu, name='admin_menu'),
    path('user/', views.userMenu, name='user_menu'),
    ]