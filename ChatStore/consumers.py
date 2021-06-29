import json
from asgiref.sync import async_to_sync
from django.contrib import auth
from django.db import connections
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime

from django.contrib.auth.models import User
from . models import Messages,Room
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
   
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        author = text_data_json['author']
        roomname = text_data_json["roomname"]

        time = (str(datetime.now()))
        user = User.objects.get(username=author)
        roomname = Room.objects.get(name=roomname)
       
        messages = Messages(author=user,content=message,room_name=roomname)
        messages.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author':author,
                'time':time,

            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        author = event['author']
        time  = event['time']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'content': message,
            'author':author,
            'time':time,
        }))