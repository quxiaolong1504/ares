# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=140)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('u_time', models.DateTimeField(auto_now=True)),
                ('device', models.CharField(max_length=50)),
                ('status', models.SmallIntegerField()),
                ('user', models.ForeignKey(related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
