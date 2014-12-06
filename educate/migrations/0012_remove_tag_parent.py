# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0011_auto_20141202_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='parent',
        ),
    ]
