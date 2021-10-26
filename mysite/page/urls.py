from django.urls import path
from django.urls import include
from page import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
