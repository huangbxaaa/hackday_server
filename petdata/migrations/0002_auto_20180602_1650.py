# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-02 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='owner',
        ),
        migrations.AddField(
            model_name='user',
            name='pet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='petdata.Pet'),
        ),
    ]
