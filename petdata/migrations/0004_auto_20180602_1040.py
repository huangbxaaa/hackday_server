# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-02 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petdata', '0003_auto_20180602_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_name',
            field=models.CharField(max_length=128, primary_key=True, serialize=False, unique=True),
        ),
    ]