from django.db import models

# Create your models here.


DEVICE_TYPES = [('iOS','iOS设备'),('Android','安卓设备')]

class Device(models.Model):
    device_token = models.CharField(max_length=100, primary_key=True)
    device_type = models.CharField(choices=DEVICE_TYPES, max_length=10)
    user_id = models.CharField(max_length=100)
    update_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    
    def is_ios(self):
        return self.device_type == "iOS"

    def is_android(self):
        return self.device_type == "Android"


class PushMessage(models.Model):
    alert = models.CharField(max_length=256)
    devices = models.ManyToManyField(Device)
    user_ids = models.CharField(max_length=100000)