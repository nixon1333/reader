# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0002_auto_20170303_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedslist',
            name='name',
            field=models.CharField(default='Default', max_length=250),
            preserve_default=False,
        ),
    ]