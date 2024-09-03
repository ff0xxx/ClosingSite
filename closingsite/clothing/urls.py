from http.client import HTTPResponse

from django.contrib import admin
from django.urls import path
from clothing import views

# root - bob@mail.ru - 1234

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    path('add/', views.ClothingCreateView.as_view(), name='add')
]
