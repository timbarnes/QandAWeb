# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0007_auto_20141202_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='parent',
            field=models.ForeignKey(blank=True, to='educate.Tag', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]
