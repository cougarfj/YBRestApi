# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-09-30 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_token', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('device_type', models.CharField(choices=[('iOS', 'iOS设备'), ('Android', '安卓设备')], max_length=10)),
                ('user_id', models.CharField(max_length=100)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        )
    ]
