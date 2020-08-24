
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/orders', views.apiOrders, name="apis"),
    path('', views.index, name='index'),
    path('simple_upload', views.simple_upload)
]
