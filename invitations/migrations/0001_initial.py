# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('contributor', 'Contributor'), ('watcher', 'Watcher')], default='watcher', max_length=255)),
                ('accepted', models.BooleanField(default=False)),
                ('expiration_days', models.PositiveSmallIntegerField(default=3)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
