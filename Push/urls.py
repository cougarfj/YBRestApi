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
    url(r'^list',views.DeviceListView.as_view()),
    url(r'^register_device',views.RegisterDeviceView.as_view()),
    url(r'^unregister_device',views.UnRegisterDeviceView.as_view()),
    url(r'^web',views.NotifyOpenWebView.as_view()),
    url(r'^live',views.NotifyOpenLiveRoom.as_view()),
    url(r'^team',views.NotifyOpenTeamHall.as_view())
]