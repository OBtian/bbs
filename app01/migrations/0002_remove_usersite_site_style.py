# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2022-04-15 10:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersite',
            name='site_style',
        ),
    ]
