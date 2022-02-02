from channels.routing import ProtocolTypeRouter,URLRouter
import websocket.routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        websocket.routing.websocket_urlpatterns
    )
})