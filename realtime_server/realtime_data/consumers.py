from channels.generic.websocket import WebsocketConsumer
import json

class RealtimeConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.channel_layer.group_add("realtime_group", self.channel_name)

    def disconnect(self, close_code):
        self.channel_layer.group_discard("realtime_group", self.channel_name)

    def realtime_message(self, event):
        message = {
            'value': event['value'],
            'timestamp': event['timestamp']
        }
        self.send(text_data=json.dumps(message))
