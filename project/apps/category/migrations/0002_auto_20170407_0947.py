# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-07 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
