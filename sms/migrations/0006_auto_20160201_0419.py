# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_auto_20160201_0417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='id_del',
            new_name='is_del',
        ),
    ]
