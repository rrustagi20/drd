# Generated by Django 3.0.3 on 2023-03-08 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
