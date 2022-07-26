from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name="login"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/', views.home, name="home"),
]
