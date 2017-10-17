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
from .models import Course,Lesson,Comment


class CourseSerializer(serializers.ModelSerializer):
    lesson_nums = serializers.
    class Meta:
        model = Course

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment





