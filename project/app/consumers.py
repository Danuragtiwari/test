import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Transcription

class TranscriptionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'transcription_group'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        transcription = json.loads(text_data)['transcription']
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'transcription_message', 'transcription': transcription}
        )

    async def transcription_message(self, event):
        transcription = event['transcription']
        await self.send(text_data=json.dumps({'transcription': transcription}))
        Transcription.objects.create(text=transcription)
