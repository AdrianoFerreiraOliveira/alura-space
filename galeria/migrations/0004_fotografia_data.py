# Generated by Django 4.1.7 on 2023-03-14 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
