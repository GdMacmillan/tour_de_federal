# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 04:33
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0006_auto_20170804_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaraunt',
            name='opening_hours',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
    ]
