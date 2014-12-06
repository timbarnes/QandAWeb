# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0003_auto_20141130_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-edit_date']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['question']},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['name']},
        ),
    ]
