# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_owner', models.CharField(max_length=255)),
                ('client_name', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('tech_stack', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]
