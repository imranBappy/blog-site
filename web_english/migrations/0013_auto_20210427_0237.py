# Generated by Django 3.2 on 2021-04-26 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_english', '0012_alter_blog_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Android_stor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50)),
                ('app_category', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('image', models.ImageField(default='static/Android_stor/', upload_to='static/profile/')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 2, 37, 19, 152280)),
        ),
    ]