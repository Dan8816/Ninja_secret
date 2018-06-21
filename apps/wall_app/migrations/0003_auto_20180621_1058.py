# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-21 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0002_auto_20180620_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='likes',
            field=models.ManyToManyField(related_name='likes_msg', to='wall_app.User'),
        ),
    ]
