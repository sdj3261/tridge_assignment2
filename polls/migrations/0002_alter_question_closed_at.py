# Generated by Django 3.2.9 on 2021-11-28 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='closed_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 1, 22, 0, 37, 713817)),
        ),
    ]
