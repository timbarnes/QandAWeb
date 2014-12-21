# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('educate', '0003_auto_20141214_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('articles', models.ManyToManyField(to='educate.Article')),
                ('categories', models.ManyToManyField(to='educate.Category')),
                ('subjects', models.ManyToManyField(to='educate.Subject')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', tinymce.models.HTMLField()),
                ('edit_date', models.DateField(auto_now=True)),
                ('slug', models.SlugField()),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'/media/profilepics/')),
                ('home', models.CharField(max_length=100)),
                ('interests', models.CharField(max_length=200)),
                ('objectives', models.CharField(max_length=200)),
                ('joined', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.CharField(max_length=200)),
                ('due', models.DateField()),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='tasklist',
            field=models.ForeignKey(to='users.TaskList'),
            preserve_default=True,
        ),
    ]
