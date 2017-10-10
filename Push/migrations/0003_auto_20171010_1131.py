# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-10 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Push', '0002_openwebmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openwebmessage',
            name='devices',
            field=models.ManyToManyField(related_name='push_openwebmessage_related', to='Push.Device'),
        ),
    ]
