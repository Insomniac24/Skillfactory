# Generated by Django 4.1.1 on 2022-10-03 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0003_remove_post_price_remove_post_quantity_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='date published'),
        ),
    ]
