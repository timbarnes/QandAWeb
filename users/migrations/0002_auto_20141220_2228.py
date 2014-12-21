# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='articles',
            field=models.ManyToManyField(to=b'educate.Article', blank=True),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='categories',
            field=models.ManyToManyField(to=b'educate.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='subjects',
            field=models.ManyToManyField(to=b'educate.Subject', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='objectives',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to=b'/media/profilepics/', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateField(blank=True),
        ),
    ]
