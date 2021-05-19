# Generated by Django 3.2 on 2021-04-26 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_english', '0013_auto_20210427_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 3, 24, 39, 842216)),
        ),
    ]
