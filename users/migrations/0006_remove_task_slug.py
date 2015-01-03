# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20141231_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='slug',
        ),
    ]
