# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 16:26
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0010_auto_20170804_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaraunt',
            name='review',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
