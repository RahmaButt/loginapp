from django.urls import path
from .views import NotFoundView

from . import views

urlpatterns = [
    path('', views.index, name="signup-page"),
    path('login', views.loginPage, name="login-page"),
    path('home', views.homePage, name="home-page"),
    path('404/', NotFoundView.as_view()),
]