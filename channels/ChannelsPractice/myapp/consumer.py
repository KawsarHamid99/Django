from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("-----------------------------------------------------")
        self.send({
            'type':'websocket.accept'
        })
        print('websocket sync Consumer connected...',event)
    
    def websocket_receive(self,event):
        print('websocket sync consumer received...',event)
        print(event["text"])
        for i in range(10):
            self.send({
                'type':'websocket.send',
                'text':str(i),
            })
            sleep(1)
    def websocket_disconnect(self,event):
        print('websocket Sync Consumer disconnected...',event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send({
            'type':'websocket.accept'
        })
        print('websocket AsyncConsumer connect ',event)

    async def websocket_receive(self,event):
        print('websocket AsyncConsumer recieved',event)
        print('connect...',event['text'])
        for i in range(20):
            await self.send({
                'type':'websocket.send',
                'text':str(i),
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self,event):
        print('websocket asyncconsumer disconnected',event)
        raise StopConsumer()
    

