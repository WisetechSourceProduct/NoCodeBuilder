# Generated by Django 5.0.4 on 2024-05-29 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoCodeBuilderApp', '0003_alter_pages_created_at_alter_pages_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 18, 30, 12, 181781)),
        ),
        migrations.AlterField(
            model_name='pages',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 29, 18, 30, 12, 181781)),
        ),
    ]
