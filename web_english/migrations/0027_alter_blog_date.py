# Generated by Django 3.2 on 2021-05-01 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_english', '0026_auto_20210430_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 2, 29, 39, 916775)),
        ),
    ]
