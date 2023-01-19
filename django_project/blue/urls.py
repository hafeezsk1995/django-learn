from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('blue_create/', views.CreateBlue.as_view(), name='blue-about'),
    path('blue_get/', views.GetBlue.as_view(), name='blue-about'),
    ]