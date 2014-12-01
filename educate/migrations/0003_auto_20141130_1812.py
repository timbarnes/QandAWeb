# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0002_auto_20141130_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='edit_date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
