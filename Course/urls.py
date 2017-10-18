#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Tue Oct 17 2017
# File: url.py
# 
# Description: 
#
from django.conf.urls import url
from .views import CourseList,CourseDetail

urlpatterns = [
    url(r'^list',CourseList.as_view()),
    url(r'^detail',CourseDetail.as_view()),
]