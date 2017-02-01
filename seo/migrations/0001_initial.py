# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=68, verbose_name='Title')),
                ('keywords', models.CharField(blank=True, max_length=100, verbose_name='Keywords')),
                ('description', models.CharField(blank=True, max_length=155, verbose_name='Description')),
                ('breadcrumb', models.CharField(blank=True, max_length=100, verbose_name='Breadcrumb')),
                ('header', models.CharField(blank=True, max_length=100, verbose_name='Header')),
                ('robots', models.CharField(blank=True, choices=[(b'index, follow', 'Index, Follow'), (b'noindex, nofollow', 'No Index, No Follow'), (b'index, nofollow', 'Index, No Follow'), (b'noindex, follow', 'No Index, Follow')], default=b'index, follow', max_length=30, verbose_name='Robots')),
            ],
            options={
                'verbose_name': 'Page meta',
                'verbose_name_plural': 'Pages meta',
            },
        ),
    ]
