from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('Home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('login/', views.loginhandle, name="search"),
    path('logout/', views.logouthandle, name="logout"),
    path('signup/', views.signuphandle, name="signup"),
    



    ]