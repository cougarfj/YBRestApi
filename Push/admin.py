from django.contrib import admin

# Register your models here.

from .models import Device,OpenWebMessage




class OpenWebMessageAdmin(admin.ModelAdmin):
    fields = ('url','alert','devices')
    filter_horizontal = ('devices',)

admin.site.register(OpenWebMessage,OpenWebMessageAdmin)


class DeviceAdmin(admin.ModelAdmin):
    date_hierarchy = 'update_time'
    list_display = ('device_token','device_type','user_id','update_time','is_delete')
    list_filter = ('device_type','update_time','is_delete')
    ordering = ['update_time']
    search_fields = ['user_id']
    actions = ['send_push']

    def send_push(self, request, queryset):
        user_ids = None
        for device in queryset:
            if user_ids == None:
                user_ids =  device.user_id
            else:
                user_ids = user_ids +  "," + device.user_id

        self.message_user(request,user_ids)

    send_push.short_description = "获取user_ids"

admin.site.register(Device,DeviceAdmin)
