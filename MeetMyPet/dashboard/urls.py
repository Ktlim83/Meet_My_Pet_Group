from django.urls import path
from . import views

urlpatterns = [
    # HOME PAGE 
    path('', views.base, name='base'),
    # PROFILE PAGE RENDER 
    path('profile/', views.profile, name='profile'),
    
    
    # LOGS OUT THE USER 
    path('logout/', views.logout, name='logout'),
    
]