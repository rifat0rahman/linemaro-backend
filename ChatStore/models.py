from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.TextField(max_length=200)
    author1 = models.ForeignKey(User, related_name='users1_room', on_delete=models.CASCADE)
    author2 = models.ForeignKey(User, related_name='users2_room', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Messages(models.Model):
    author = models.ForeignKey(User,related_name="user_msg", on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(default=datetime.now, blank=True)
    room_name = models.ForeignKey(Room, related_name='room_msg',default=1, on_delete=models.CASCADE)
