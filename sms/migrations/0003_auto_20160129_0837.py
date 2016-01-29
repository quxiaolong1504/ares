# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_message_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='text',
            new_name='msg',
        ),
    ]
