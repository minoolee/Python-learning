from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('home/', views.home),
    path('about', views.about)
]