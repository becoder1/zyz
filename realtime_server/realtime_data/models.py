from django.db import models

# Create your models here.
class RandomNumber(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)