# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20170715_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='title',
            field=models.CharField(blank=True, choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=3),
        ),
    ]
