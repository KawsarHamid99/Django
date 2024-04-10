from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio


class MySyncCunsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("websocket sync consumer connected...",event)
        self.send({
            'type': 'websocket.accept'
        })
        print("websocket sync consumer connected...",event)


    def websocket_receive(self,event):
        print('websocket sync consumer recieved...',event)
        for i in range(15):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            sleep(1)

    def websocket_disconnect(self,event):
        print('websocket sync consumer disconnected...',event)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):

        await self.send({
            'type':'websocket.accept'
        })
        print("Asyncconsumer Connected...",event)
    
    async def websocket_receive(self,event):
        print("websocket AsyncConsumer Recieved...",event)
        for i in range(10):
            await self.send({
                'type':'websocket.send',
                'text':str(i),
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self,event):
        print("websocket SyncConsumer Disconnected",event)
        raise StopConsumer()