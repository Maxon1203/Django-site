# Generated by Django 3.2.7 on 2022-04-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20220407_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag_duraction',
        ),
        migrations.AddField(
            model_name='post',
            name='tag_state',
            field=models.ManyToManyField(blank=True, related_name='post', to='news.Tag', verbose_name='Тэг'),
        ),
    ]