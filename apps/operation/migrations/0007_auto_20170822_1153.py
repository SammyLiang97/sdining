# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-22 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_order_is_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, max_length=100, verbose_name='评价'),
        ),
    ]