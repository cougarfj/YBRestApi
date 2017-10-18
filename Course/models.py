from django.db import models

# Create your models here.



class Course(models.Model):
    name = models.CharField(max_length=100)
    introduce = models.TextField()
    price = models.IntegerField()
    buy_nums = models.IntegerField()
    teacher_avatar = models.URLField()
    teacher_name = models.CharField(max_length=100)
    teacher_title = models.CharField(max_length=100)   #职称
    created_time = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    price = models.IntegerField()
    hasBuy = models.BooleanField()
    course = models.ForeignKey(Course)
    video_url = models.URLField()
    created_time = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    
    star_nums = models.IntegerField()
    course = models.ForeignKey(Course)
    content = models.TextField()
    user_id = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)


