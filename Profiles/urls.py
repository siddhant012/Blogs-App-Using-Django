from django.urls import path, include
from .import views as profile_views

urlpatterns = [
    #path('create/', profile_views.CreateProfileView, name='profile_create_view' ), 
    path('update/', profile_views.UpdateProfileView, name='profile_update_view' ),
    path('<str:username>/', profile_views.ProfileView, name='profile_view' ),
    #path('<str:username>/delete/', profile_views.DeleteProfileView, name='profile_delete_view' ),
]
