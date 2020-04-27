# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-27 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20200427_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('albania', 'Albania'), ('algeria', 'Algeria'), ('andorra', 'Andorra'), ('argentina', 'Argentina'), ('armenia', 'Armenia'), ('australia', 'Australia'), ('austria', 'Austria'), ('azerbaijan', 'Azerbaijan'), ('belarus', 'Belarus'), ('belgium', 'Belgium'), ('bermuda', 'Bermuda'), ('bosnia', 'Bosnia'), ('brazil', 'Brazil'), ('bulgaria', 'Bulgaria'), ('canada', 'Canada'), ('chile', 'Chile'), ('china', 'China'), ('colombia', 'Colombia'), ('costa_rica', 'Costa Rica'), ('croatia', 'Croatia'), ('cyprus', 'Cyprus'), ('czech_republic', 'Czech Republic'), ('denmark', 'Denmark'), ('ecuador', 'Ecuador'), ('egypt', 'Egypt'), ('estonia', 'Estonia'), ('finland', 'Finland'), ('france', 'France'), ('georgia', 'Georgia'), ('germany', 'Germany'), ('greece', 'Greece'), ('guatemala', 'Guatemala'), ('honduras', 'Honduras'), ('hungary', 'Hungary'), ('iceland', 'Iceland'), ('india', 'India'), ('indonesia', 'Indonesia'), ('israel', 'Israel'), ('italy', 'Italy'), ('jamaica', 'Jamaica'), ('japan', 'Japan'), ('latvia', 'Latvia'), ('liechtenstein', 'Liechtenstein'), ('lithuania', 'Lithuania'), ('luxembourg', 'Luxembourg'), ('macedonia', 'Macedonia'), ('malaysia', 'Malaysia'), ('maldives', 'Maldives'), ('malta', 'Malta'), ('mexico', 'Mexico'), ('moldova', 'Moldova'), ('monaco', 'Monaco'), ('montenegro', 'Montenegro'), ('morocco', 'Morocco'), ('netherlands', 'Netherlands'), ('new_zealand', 'New Zealand'), ('norway', 'Norway'), ('peru', 'Peru'), ('philippines', 'Philippines'), ('poland', 'Poland'), ('portugal', 'Portugal'), ('south_korea', 'Republic of Korea'), ('romania', 'Romania'), ('russia', 'Russia'), ('serbia', 'Serbia'), ('singapore', 'Singapore'), ('slovakia', 'Slovakia'), ('slovenia', 'Slovenia'), ('south_africa', 'South Africa'), ('spain', 'Spain'), ('sweden', 'Sweden'), ('switzerland', 'Switzerland'), ('thailand', 'Thailand'), ('tunisia', 'Tunisia'), ('turkey', 'Turkey'), ('ukraine', 'Ukraine'), ('uae', 'United Arab Emirates'), ('uk', 'United Kingdom'), ('usa', 'United States')], max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]