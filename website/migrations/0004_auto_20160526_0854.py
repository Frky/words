# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160526_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
