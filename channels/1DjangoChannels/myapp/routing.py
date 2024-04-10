from django.urls import path
from myapp import consumers

websocket_urlpatterns=[
    path('ws/sc/',consumers.MySyncCunsumer.as_asgi()),
    path('ws/as/',consumers.MyAsyncConsumer.as_asgi()),

]