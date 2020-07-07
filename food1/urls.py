from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact',views.contact,name="contact"),
    path('menu', views.menu,name="menu"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
    path('login', views.login,name="login")
]
