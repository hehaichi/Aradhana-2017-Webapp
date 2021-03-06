# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Class 1-5', 'Class 1 to 4'), ('Class 5-7', 'Class 5 to 7'), ('Class 8-10', 'Class 8 to 10')], default='Select', max_length=100)),
                ('type', models.CharField(choices=[('Individual Event', 'Individual Event'), ('Team Event', 'Team Event')], default='Select', max_length=100)),
                ('first_place', models.TextField(default='TBD')),
                ('second_place', models.TextField(default='TBD')),
                ('third_place', models.TextField(default='TBD')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('standard', models.IntegerField()),
                ('school', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('events', models.ManyToManyField(to='aradhana.Event')),
            ],
        ),
    ]
