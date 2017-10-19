from django.contrib import admin
from .models import Course,Lesson,Comment,Order,Advertisement
# Register your models here.

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Advertisement)