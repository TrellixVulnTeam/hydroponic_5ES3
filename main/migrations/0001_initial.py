# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=50)),
                ('english', models.CharField(default='', max_length=1000)),
                ('chinese', models.CharField(default='', max_length=1000)),
                ('italian', models.CharField(default='', max_length=1000)),
                ('portuguese', models.CharField(default='', max_length=1000)),
                ('slovak', models.CharField(default='', max_length=1000)),
                ('spanish', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]