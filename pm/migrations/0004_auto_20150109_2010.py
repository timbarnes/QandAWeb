# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import tinymce.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0003_auto_20150107_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateField(default=datetime.datetime(2015, 1, 10, 4, 9, 43, 899179, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='notes',
            field=tinymce.models.HTMLField(default='Notes'),
            preserve_default=False,
        ),
    ]
