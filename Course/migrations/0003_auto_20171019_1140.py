# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-19 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_auto_20171018_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, '订单完成'), (1, '等待支付'), (2, '支付取消'), (3, '订单出错')], default=1)),
                ('price', models.IntegerField()),
                ('user_id', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='Course.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='hasBuy',
        ),
        migrations.AlterField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Course.Course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='Course.Course'),
        ),
    ]