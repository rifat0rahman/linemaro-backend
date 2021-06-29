from django.urls import path
from . import views
urlpatterns = [
    path('',views.messages,name="msessages"),
    path('users/',views.users,name="users"),
    path('rooms/',views.room,name="rooms"),

]
