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
from Push import views

urlpatterns = [
    url(r'^register',views.register)
]