# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-09-29 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Push', '0002_device_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
