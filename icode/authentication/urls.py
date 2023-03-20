from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('', views.home, name="home"),
    path('index', views.index, name="index"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="index"),
    path('signout', views.signout, name="index")


]