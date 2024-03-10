from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.LoginView.as_view(), name="login"),
    path('room/',views.RoomView.as_view(),name="room"),
    path('users/',views.UserView.as_view(),name="users"),
    path('room/<str:pk>/',views.room,name="room")
]