from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [
    path('', views.userdetails),
    path('show/', views.showUser),
]
