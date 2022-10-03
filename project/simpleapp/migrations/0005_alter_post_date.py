# Generated by Django 4.1.1 on 2022-10-03 01:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0004_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
