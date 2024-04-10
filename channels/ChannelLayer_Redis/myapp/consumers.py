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
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,self.channel_name
            )
        
        self.send({
            'type':'websocket.accept'
        })
        print("consumer connected",event)

    def websocket_receive(self,event):
        print("consumer recieved...\n",event)
        print(event['text'])
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
            'type':'chat.message',
            'message':event['text']
        })
    def chat_message(self,event):
        print("--------------chat_message----------------")
        print(event)

        self.send({
            'type':'websocket.send',
            'text':event['message']
        })

        
    def websocket_disconnect(self,event):
        print('-----------------channels disconnected------------------------')
        print('websocket sync consumer disconnected...',event)
        print('channel layer...',self.channel_layer)
        print("channel name....",self.channel_name)

        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,self.channel_name
            )
        raise StopConsumer()
    





class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("-------------channel information-----------")
        print('channel layer...',self.channel_layer)
        print("channel name.....",self.channel_name)

        group_name=self.scope['url_route']['kwargs']['groupname']

        await self.channel_layer.group_add(
            'programmers',self.channel_name
            )
        
        await self.send({
            'type':'websocket.accept'
        })
        print("consumer connected",event)

    async def websocket_receive(self,event):
        print("consumer recieved...\n",event)
        print(event['text'])
        await self.channel_layer.group_send('programmers',{
            'type':'chat.message',
            'message':event['text']
        })
    async def chat_message(self,event):
        print("--------------chat_message----------------")
        print(event)

        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })

        
    async def websocket_disconnect(self,event):
        print('-----------------channels disconnected------------------------')
        print('websocket sync consumer disconnected...',event)
        print('channel layer...',self.channel_layer)
        print("channel name....",self.channel_name)

        await self.channel_layer.group_discard(
            'programmers',self.channel_name
            )
        raise StopConsumer()