from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name = 'login'),
    path('signup/', views.signUpPage, name = 'signup'),
    path('dashboard/', views.dashboardGraph, name = 'dashboard')
]