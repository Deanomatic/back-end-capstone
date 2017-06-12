# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 15:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_auto_20170612_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='created_at',
        ),
        migrations.AddField(
            model_name='reminder',
            name='time_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
