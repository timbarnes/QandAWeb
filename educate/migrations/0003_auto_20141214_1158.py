# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('educate', '0002_article_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='published',
        ),
        migrations.AddField(
            model_name='article',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('category', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('subject', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('category', 'question')]),
        ),
    ]
