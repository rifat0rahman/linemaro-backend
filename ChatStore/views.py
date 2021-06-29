from django.db import connections
from django.shortcuts import render, resolve_url
from rest_framework.decorators import api_view
from . serializers import MessagesSerializers, UserSerializers, RoomSerializers
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from . models import Messages, Room
# Create your views here.


@api_view(['GET'])
def messages(request):
    Message = Messages.objects.all()
    serializer = MessagesSerializers(Message, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserSerializers(users, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def room(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializers(rooms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data

        name = data["name"]
        author1 = User.objects.get(username=data["author1"])
        author2 = User.objects.get(username=data["author2"])

        if name and author1 and author2:
            # checking weather the two author has already created a conv
            if_it_is = str(author2)+str(author1)

            try:
                room = Room.objects.get(name=if_it_is)
                
            except:
                room, created = Room.objects.get_or_create(name=name,
                                                           author1=author1,
                                                           author2=author2)

                room.save()
            
            return Response(data=str(room), status=200)
        else:
            return Response('unsucces request', status=201)
