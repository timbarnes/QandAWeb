# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.CharField(default='Category description', max_length=200),
            preserve_default=False,
        ),
    ]
