# Generated by Django 3.2.7 on 2022-04-08 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20220408_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': (('can_see_author', 'Можно видеть автора коментария'),), 'verbose_name': 'Комментариии', 'verbose_name_plural': 'Комментариии'},
        ),
    ]
