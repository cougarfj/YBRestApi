#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Tue Oct 17 2017
# File: serializers.py
# 
# Description: 
#


from rest_framework import serializers
from .models import Course,Lesson,Comment,Order,Advertisement
from django.db.models import Avg

class CourseListSerializer(serializers.ModelSerializer):
    
    def to_representation(self, obj):
        
        return {
            'id':obj.id,
            'name':obj.name,
            'cover_url':obj.video_cover_url,
            'introduce':obj.introduce,
            'lesson_nums':Lesson.objects.filter(course=obj).count(),
            'stars_avg':Comment.objects.filter(course=obj).aggregate(Avg('star_nums')).get('star_nums__avg'),
            'price':obj.price,
            'buy_nums':Order.objects.filter(course=obj,status=0).count(),
            'teacher_avatar':obj.teacher_avatar,
            'teacher_name':obj.teacher_name,
            'teacher_title':obj.teacher_title,
            'created_time':obj.created_time
        }        

    class Meta:
        model = Course


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):

   
    def to_representation(self, obj):

        return {
                'id':obj.id,
                'name':obj.name,
                'introduce':obj.introduce,
                'lessons':LessonSerializer(Lesson.objects.filter(course=obj), many=True).data,
                'stars_avg':Comment.objects.filter(course=obj).aggregate(Avg('star_nums')).get('star_nums__avg'),
                'buy_nums':Order.objects.filter(course=obj,status=0).count(),
                'price':obj.price,
                'buy_nums':Order.objects.filter(course=obj,status=0).count(),
                'teacher_avatar':obj.teacher_avatar,
                'teacher_name':obj.teacher_name,
                'teacher_title':obj.teacher_title,
                'created_time':obj.created_time
        }  
    
    class Meta:
        model = Course


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'




