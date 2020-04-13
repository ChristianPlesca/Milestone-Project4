# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-11 19:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200411_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofilepic', to=settings.AUTH_USER_MODEL),
        ),
    ]
