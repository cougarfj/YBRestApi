from django.db import models
from Push.constant import *
# Create your models here.


DEVICE_TYPES = [('iOS','iOS设备'),('Android','安卓设备')]

class Device(models.Model):
    device_token = models.CharField(max_length=100, primary_key=True)
    device_type = models.CharField(choices=DEVICE_TYPES, max_length=10)
    user_id = models.CharField(max_length=100)
    update_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.device_token

    def is_ios(self):
        return self.device_type == "iOS"

    def is_android(self):
        return self.device_type == "Android"



class PushMessage(models.Model):
    alert = models.CharField(max_length=500)
    push_id = models.CharField(max_length=100)
    devices = models.ManyToManyField(Device,related_name="%(app_label)s_%(class)s_related")
    custom_data = models.CharField(max_length=1000)

    class Meta:
        abstract = True

class OpenWebMessage(PushMessage):
    url = models.CharField(max_length=500)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.custom_data = {"action":PUSH_ACTION_OPEN_WEBVIEW,"data":{"url":self.url}}
    