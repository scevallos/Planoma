# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 04:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
