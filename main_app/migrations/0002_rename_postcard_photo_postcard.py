# Generated by Django 5.0.4 on 2024-04-11 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='PostCard',
            new_name='postcard',
        ),
    ]
