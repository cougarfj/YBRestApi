from django.contrib import admin

# Register your models here.

from .models import Device,OpenWebMessage




class OpenWebMessageAdmin(admin.ModelAdmin):
    fields = ('url','alert','devices')
    filter_horizontal = ('devices',)

admin.site.register(OpenWebMessage,OpenWebMessageAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_token','device_type','user_id','update_time','is_delete')
    list_filter = ('device_type','update_time','is_delete')
    ordering = ['update_time']
    search_fields = ['user_id']
    actions = ['send_push']

    def send_push(self, request, queryset):
        print("send_push")

    send_push.short_description = "对选中设备发送推送"

admin.site.register(Device,DeviceAdmin)
