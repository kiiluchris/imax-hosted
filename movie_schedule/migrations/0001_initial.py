# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import movie_schedule.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('preview', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=movie_schedule.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MoviePricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_time', models.TimeField()),
                ('student_fee', models.IntegerField(blank=True, null=True)),
                ('regular_fee', models.IntegerField()),
                ('movie', models.ManyToManyField(to='movie_schedule.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieViewing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_preview_video', models.URLField()),
                ('movie_preview_poster', models.FileField(upload_to=movie_schedule.models.upload_location)),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movie_schedule.Movie')),
            ],
        ),
    ]
