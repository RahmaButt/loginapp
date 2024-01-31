from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="signup-page"),
    path('login', views.loginPage, name="login-page"),
    path('home', views.homePage, name="home-page")
    
]