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
    url(r'^filter',views.DeviceFilterView.as_view()),
    url(r'^search',views.DeviceListView.as_view()),
    url(r'^register_device',views.RegisterDeviceView.as_view()),
    url(r'^unregister_device',views.UnRegisterDeviceView.as_view()),
    url(r'^open_webview',views.NotifyOpenWebView.as_view()),
    url(r'^open_liveroom',views.NotifyOpenLiveRoom.as_view()),
    url(r'^open_teamhall',views.NotifyOpenTeamHall.as_view())
]