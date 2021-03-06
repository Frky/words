# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.CharField(db_index=True, max_length=14, primary_key=True, serialize=False, unique=True)),
                ('word', models.CharField(max_length=255)),
                ('bg_color', models.CharField(default='#ffffff', max_length=7)),
                ('fg_color', models.CharField(default='#000000', max_length=7)),
                ('top', models.IntegerField()),
                ('left', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
