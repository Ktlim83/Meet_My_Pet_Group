from django.urls import path
from . import views

# This Is A Test
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('success', views.success),
]