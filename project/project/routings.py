from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app.consumers import TranscriptionConsumer
from django.core.asgi import get_asgi_application
application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': URLRouter([path('ws/transcription/', TranscriptionConsumer.as_asgi())]),
    }
)
