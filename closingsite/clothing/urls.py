from http.client import HTTPResponse

from django.contrib import admin
from django.urls import path
from clothing import views


app_name = 'clothing'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
