# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirror', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='description',
            field=models.CharField(default='some text', max_length=500),
        ),
    ]
