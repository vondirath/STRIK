# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_posts_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='inventory',
            field=models.CharField(max_length=5),
        ),
    ]