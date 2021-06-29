from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import  User
from . models import Messages,Room

class MessagesSerializers(serializers.ModelSerializer):
    author = serializers.CharField()
    room_name = serializers.CharField(source='room_name.name')

    class Meta:
        model=Messages
        fields=('id','author','content','time','room_name')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email']

class RoomSerializers(serializers.ModelSerializer):
    author1 = serializers.CharField()
    author2 = serializers.CharField()
    class Meta:
        model = Room
        fields = '__all__'