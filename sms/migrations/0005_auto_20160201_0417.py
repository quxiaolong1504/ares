# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_auto_20160129_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='status',
        ),
        migrations.AddField(
            model_name='message',
            name='id_del',
            field=models.SmallIntegerField(default=0),
        ),
    ]
