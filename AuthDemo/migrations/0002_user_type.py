# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-12 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthDemo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, 'vip'), (2, '普通用户'), (3, 'vvip')], default=2),
        ),
    ]
