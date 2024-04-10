import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChannels_1.settings')
import myapp.routing
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        myapp.routing.websocket_urlpatterns
    )

})
