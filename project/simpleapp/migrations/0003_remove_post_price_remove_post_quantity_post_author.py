# Generated by Django 4.1.1 on 2022-10-02 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simpleapp', '0002_post_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='price',
        ),
        migrations.RemoveField(
            model_name='post',
            name='quantity',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор поста'),
        ),
    ]