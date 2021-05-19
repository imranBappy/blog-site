# Generated by Django 3.2 on 2021-04-30 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_english', '0024_auto_20210430_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='content_1',
            name='button_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='content_2',
            name='button_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 23, 46, 49, 619319)),
        ),
        migrations.AlterField(
            model_name='content_1',
            name='image1',
            field=models.ImageField(default='', upload_to='static/content/'),
        ),
        migrations.AlterField(
            model_name='content_1',
            name='image2',
            field=models.ImageField(default='', upload_to='static/content/'),
        ),
        migrations.AlterField(
            model_name='content_1',
            name='subtitel',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='content_1',
            name='subtitle2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='content_1',
            name='titel',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='content_2',
            name='image1',
            field=models.ImageField(default='', upload_to='static/content/'),
        ),
        migrations.AlterField(
            model_name='content_2',
            name='image2',
            field=models.ImageField(default='', upload_to='static/content/'),
        ),
        migrations.AlterField(
            model_name='content_2',
            name='subtitel',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='content_2',
            name='subtitle2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='content_2',
            name='titel',
            field=models.CharField(default='', max_length=100),
        ),
    ]