# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0004_auto_20141201_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2014, 12, 2, 8, 0, 23, 299363, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
