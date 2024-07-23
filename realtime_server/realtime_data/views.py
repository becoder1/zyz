from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random
import json
# Create your views here.
from django.shortcuts import render



@csrf_exempt
def generate_random_number(request):
    if request.method == 'POST':
        # Generate a random number
        random_number = random.randint(1, 100)

        # Save to database
        from .models import RandomNumber
        RandomNumber.objects.create(value=random_number)

        # Push data to WebSocket clients
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "realtime_group",
            {
                "type": "realtime_message",
                "value": random_number,
                "timestamp": now().isoformat()
            }
        )

        return HttpResponse("Random number generated and sent to clients.")
    else:
        return HttpResponse("Only POST requests are allowed.")

def index(request):
    return render(request, 'index.html')