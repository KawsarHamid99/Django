
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import RoutingApp.routing  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoRouting.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        RoutingApp.routing.websocket_urlpatterns
    )
})
