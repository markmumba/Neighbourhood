# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-15 19:51
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0004_auto_20190915_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]