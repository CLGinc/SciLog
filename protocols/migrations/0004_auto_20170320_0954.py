# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocols', '0003_auto_20170320_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='text',
            field=models.CharField(max_length=1024),
        ),
    ]
