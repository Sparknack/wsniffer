# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wshark', '0002_auto_20171127_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcpm',
            name='next_proto',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
