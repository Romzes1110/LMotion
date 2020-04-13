# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-07 19:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200407_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 7, 22, 34, 24, 824113), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 7, 22, 34, 24, 824113), verbose_name='Дата'),
        ),
    ]
