from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("-------------channel information-----------")
        print('channel layer...',self.channel_layer)
        print("channel name.....",self.channel_name)

        async_to_sync(self.channel_layer.group_add)(
            'programmers',self.channel_name
            )
        
        self.send({
            'type':'websocket.accept'
        })
        print("consumer connected",event)

    def websocket_receive(self,event):
        print("consumer recieved...",event)
        print(event['text'])
        
    def websocket_disconnect(self,event):
        print('-----------------channels disconnected------------------------')
        print('websocket sync consumer disconnected...',event)
        print('channel layer...',self.channel_layer)
        print("channel name....",self.channel_name)

        async_to_sync(self.channel_layer.group_discard)(
            'programmers',self.channel_name
            )
        raise StopConsumer()