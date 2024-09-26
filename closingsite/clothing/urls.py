from django.urls import path
from clothing import views


app_name = 'clothing'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
]
