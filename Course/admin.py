from django.contrib import admin
from .models import Course,Lesson,Comment
# Register your models here.

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)