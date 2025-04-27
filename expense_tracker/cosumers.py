from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer 
from asgiref.sync import async_to_sync
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()


        # Отправляем сообщение о подключении
        await self.send(text_data=json.dumps({"message": "Подключение успешно"}))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications", self.channel_name)


    async def send_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))


    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')
        await self.send(text_data=json.dumps({"message": f"Ответ: {message}"}))


    def notify_all_users(message): 
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send) ( 
            "notifications",
            {"type": "send_message", "message": message}
        )
