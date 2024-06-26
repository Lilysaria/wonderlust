# Generated by Django 4.2.11 on 2024-04-12 18:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='address',
        ),
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
        migrations.RemoveField(
            model_name='location',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='location',
            name='edited_at',
        ),
        migrations.RemoveField(
            model_name='location',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='location',
            name='lati',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AddField(
            model_name='location',
            name='longi',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)]),
        ),
    ]
