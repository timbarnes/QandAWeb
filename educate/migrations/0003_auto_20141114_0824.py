# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0002_category_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(default=b'-description-', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_text',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='answer_text',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_description',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=b'-description-', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='subject',
            field=models.ForeignKey(default=0, to='educate.Subject'),
            preserve_default=False,
        ),
    ]
