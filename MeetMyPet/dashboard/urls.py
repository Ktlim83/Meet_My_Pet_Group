from django.urls import path
from . import views

urlpatterns = [
    # HOME PAGE 
    path('', views.base, name='base'),
    # PROFILE PAGE RENDER 
    path('profile/<int:id>', views.profile, name='profile'),
    # ADOPT PAGE RENDER 
    path('adopt/', views.adopt, name='adopt'),
    # EDITS THE PROFILE INFO 
    path('edit_profile/<int:id>', views.edit_profile, name="edit_profile"),
    
    
    
    
    # MESSAGEBOARD PAGE RENDER 
    path('messageboard/', views.messageboard, name='messageboard'),
    # CREATE A POST
    path('create', views.createPost),
    # DELETE A POST
    path('<int:post_id>/delete', views.deletePost),
    # LIKE A POST
    path('<int:post_id>/like', views.likePost),
    # CREATE A COMMENT
    path('<int:post_id>/create_comm', views.createComm),
    # DELETE A COMMENT
    path('<int:comment_id>/deleteComm', views.deleteComm),
    
    
    # LOGS OUT THE USER 
    path('logout/', views.logout, name='logout'),
    
]