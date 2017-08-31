#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# Date: Fri Aug 25 2017
# File: urls.py
# 
# Description: 
#


from django.conf.urls import url
from Notify import views

urlpatterns = [
    url(r'^live',views.live),
    url(r'^web',views.web),
    url(r'^team',views.team),
]