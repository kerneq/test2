# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirror', '0009_auto_20170118_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesrus',
            name='nameEng',
            field=models.CharField(default='name', max_length=200),
        ),
        migrations.AlterField(
            model_name='seriesrus',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/img/holder'),
        ),
    ]