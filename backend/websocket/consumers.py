from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from .models import Alarm
from api_module import shelter, inquiry_response_heatwave


@receiver(post_save, sender=Alarm)
def announce_likes(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "shares", {
                "type": "share_message",
                "message": instance.message,
                "la": instance.la,
                "lo": instance.lo,  # 여기서 받고
            }
        )


class UserTestConsumer(WebsocketConsumer):
    def connect(self):
        self.groupname = "shares"
        self.accept()
        print('connect successful')

        async_to_sync(self.channel_layer.group_add)(
            self.groupname,
            self.channel_name
        )

    def receive(self, text_data):  # 받을 정보 여기에다가 parsing
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        content = text_data_json['content']
        print("received message : " + message)
        async_to_sync(self.channel_layer.group_send)(
            self.groupname,
            {
                'type': 'share_message',
                'message': message,
                'content': content
            }
        )

    def share_message(self, event):  # 여기다 정보 모아서 보내면됨 쉼터, 행동요령 보낼예정?
        message = event['message']
        latitude = event['la']
        longitude = event['lo']
        shelters = shelter.find_short(longitude, latitude)  # 받아온 좌표인자 parameter로 넣을예정
        inquiry = inquiry_response_heatwave.get_action_by_field('public')  # 종사하는 field 받아와서 넣을예정
        text_data = json.dumps({
            'message': message,
            'shelters': shelters,
            'inquiry': inquiry[0],
            'la' : str(latitude),
            'lo' : str(longitude),
        })
        self.send(text_data)
