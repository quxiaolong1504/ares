# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_auto_20160201_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='is_del',
            field=models.BooleanField(default=False),
        ),
    ]
