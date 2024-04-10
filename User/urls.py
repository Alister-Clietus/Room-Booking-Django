from django.urls import path
from .views import create_user,create_room,delete_room,edit_room,edit_user,get_all_users,get_all_rooms

urlpatterns = [
    path('user/create/', create_user, name='create_user'),
    path('room/create/', create_room, name='create_room'),
    path('room/delete/<int:room_id>/', delete_room, name='delete_room'),
    path('room/edit/<str:room_number>/', edit_room, name='edit_room'),
    path('user/edit/<str:username>/', edit_user, name='edit_user'),
    path('user/all/', get_all_users, name='get_all_users'),
    path('room/all/', get_all_rooms, name='get_all_rooms'),



]
