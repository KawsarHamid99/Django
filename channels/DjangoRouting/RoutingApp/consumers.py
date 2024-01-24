from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.send({
            'type':'websocket.accept'
        })
        print('websocket Sync Consumer connected...',event)


    def websocket_receive(self,event):
        print('websocket Sync Consumer recieved...',event)
        print(event['text'])
        for i in range(10):
            self.send({
                'type':'websocket.send',
                'text':str(i),
            })
            sleep(1)


    def websocket_disconnect(self,event):
        print('websocket Sync Consumer disconnected...',event)
        raise StopConsumer()
     
class MyAyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send({
            'type':'websocket.accept'
        })  
        print('websocket SyncConsumer connected',event)
    async def websocket_receive(self,event):
        print('websocket SyncConsumer recieved',event)
        print('connected...',event['text'])
        for i in range(50):
            await self.send({
                'type':'websocket.send',
                'text': str(i),
            })
            await asyncio.sleep(1)
    async def websocket_disconnect(self,event):
        print('websocket SyncConsumer disconnected',event)
        raise StopConsumer()