# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 04:35
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0009_auto_20170804_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaraunt',
            name='photos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
    ]
