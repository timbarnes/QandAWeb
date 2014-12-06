# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0012_remove_tag_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
