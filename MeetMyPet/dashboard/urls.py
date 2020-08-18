from django.urls import path
from . import views

urlpatterns = [
    # HOME PAGE 
    path('', views.base, name='base'),
    # PROFILE PAGE RENDER 
    path('profile/', views.profile, name='profile'),
    # EDITS THE PROFILE INFO 
    path('edit_profile/<int:id>', views.edit_profile, name="edit_profile"),
    
    
    # MESSAGEBOARD PAGE RENDER 
    path('messageboard/', views.messageboard, name='messageboard'),
    
    
    
    # LOGS OUT THE USER 
    path('logout/', views.logout, name='logout'),
    
]