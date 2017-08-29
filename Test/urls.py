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
from Test import views

urlpatterns = [
    url(r'^push/message_to_all',views.message_to_all),
    url(r'^push/message_to_one',views.message_to_one),
    url(r'^push/message_to_multiple',views.message_to_multiple)
]