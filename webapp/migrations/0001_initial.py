# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-13 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
    ]
