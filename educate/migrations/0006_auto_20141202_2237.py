# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0005_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(to='educate.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='educate.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='tags',
            field=models.ManyToManyField(to='educate.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='educate.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='tags',
            field=models.ManyToManyField(to='educate.Tag'),
            preserve_default=True,
        ),
    ]
