from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about-us/', views.about, name="about"),
    path('sign-up/', views.registerPage, name="sign"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout")
]
