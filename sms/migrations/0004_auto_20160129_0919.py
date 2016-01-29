# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20160129_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
