# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_task_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='resolution',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateField(null=True, blank=True),
        ),
    ]
