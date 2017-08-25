from django.db import models

# Create your models here.


DEVICE_TYPES = [('iOS','iOS设备'),('Android','安卓设备')]

class Device(models.Model):
    device_token = models.CharField(max_length=100, primary_key=True)
    device_type = models.CharField(choices=DEVICE_TYPES, max_length=10)
    user_id = models.IntegerField()