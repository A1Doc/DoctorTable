from django.urls import path
from .views import normal
urlpatterns = [
path("hello",normal)
]