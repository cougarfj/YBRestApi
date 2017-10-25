from django.db import models

# Create your models here.



class Course(models.Model):
    name = models.CharField(max_length=100)
    introduce = models.TextField()
    is_recommend = models.BooleanField()  #是否是热门推荐
    video_cover_url = models.URLField(blank=True)
    price = models.IntegerField()
    teacher_avatar = models.URLField()
    teacher_name = models.CharField(max_length=100)
    teacher_title = models.CharField(max_length=100)   #职称
    created_time = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    price = models.IntegerField()
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    video_url = models.URLField()
    video_thumb_url = models.URLField(blank=True)
    created_time = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    
    star_nums = models.IntegerField()
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    user_id = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)



class Order(models.Model):

    STATUS_TYPE = [
        (0,"订单完成"),
        (1,"等待支付"),
        (2,"支付取消"),
        (3,"订单出错")
    ]

    course = models.ForeignKey(Course,related_name="orders", on_delete=models.CASCADE)
    status= models.IntegerField(choices=STATUS_TYPE,default=1)
    price = models.IntegerField()
    user_id = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    thumb_image_url = models.URLField()
    created_time = models.DateTimeField(auto_now=True)
    is_show = models.BooleanField()  ##是否显示


    