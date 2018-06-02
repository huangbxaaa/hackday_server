# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-02 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(default='0', max_length=128, primary_key=True, serialize=False, verbose_name='user_name')),
                ('email', models.CharField(default='0', max_length=128, unique=True, verbose_name='email')),
                ('password', models.IntegerField(default=1)),
            ],
        ),
    ]
