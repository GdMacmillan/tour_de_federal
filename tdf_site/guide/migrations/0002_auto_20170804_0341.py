# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaraunt',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
