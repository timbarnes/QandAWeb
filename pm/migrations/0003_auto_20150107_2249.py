# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0002_auto_20150107_2247'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='note',
            unique_together=set([('project', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='tasklist',
            unique_together=set([('project', 'slug')]),
        ),
    ]
