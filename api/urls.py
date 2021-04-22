from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('schedules/', views.index, name="home"),
    path('sign-up/', views.registerPage, name="sign"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout")
]
