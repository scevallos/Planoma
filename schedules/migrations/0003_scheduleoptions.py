# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_schedule_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleOptions',
            fields=[
                ('schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='schedules.Schedule')),
                ('existing_credits', models.CharField(choices=[(b'ZERO', b'0'), (b'ONE', b'1'), (b'TWO', b'2')], max_length=12)),
                ('languages_completed', models.CharField(choices=[(b'ZERO', b'0'), (b'ONE', b'1'), (b'TWO', b'2'), (b'THREE', b'3')], max_length=12)),
                ('math_completed', models.CharField(choices=[(b'NONE', b'None'), (b'CALC1', b'Calc I'), (b'CALC2', b'Calc II'), (b'LINEAR', b'Linear+')], max_length=12)),
            ],
        ),
    ]