# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synenosis', '0010_auto_20160424_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='swift_bic',
            field=models.CharField(blank=True, max_length=128, verbose_name=b'Swift code'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='type',
            field=models.CharField(max_length=128, verbose_name=b'Type'),
        ),
    ]
