# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2022-04-19 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20220419_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=256, verbose_name='文章简介'),
        ),
    ]
