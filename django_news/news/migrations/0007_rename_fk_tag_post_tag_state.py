# Generated by Django 3.2.7 on 2022-04-07 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_post_fk_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='fk_tag',
            new_name='tag_state',
        ),
    ]