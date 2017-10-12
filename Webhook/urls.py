#!/usr/bin/python3
#-*- coding:utf8 -*-
#
# Author: Root
# File: urls.py
# 
# Description: 
#

from django.conf.urls import url
from Webhook import views

urlpatterns = [
    url(r'^swaggerdoc/',views.SwaggerDocDeployView.as_view()),
]