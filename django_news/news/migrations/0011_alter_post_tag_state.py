# Generated by Django 3.2.7 on 2022-04-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20220407_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag_state',
            field=models.ManyToManyField(blank=True, related_name='post', to='news.Tag', verbose_name='Тег'),
        ),
    ]
