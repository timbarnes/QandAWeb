# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'slug')]),
        ),
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tasklist',
            name='user',
        ),
        migrations.AddField(
            model_name='note',
            name='project',
            field=models.ForeignKey(default=1, to='pm.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasklist',
            name='project',
            field=models.ForeignKey(default=1, to='pm.Project'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='note',
            unique_together=set([('project', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='tasklist',
            unique_together=set([('project', 'slug')]),
        ),
    ]
