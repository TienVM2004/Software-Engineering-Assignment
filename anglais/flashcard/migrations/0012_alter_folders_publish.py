# Generated by Django 4.1.13 on 2024-04-30 23:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0011_alter_folders_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folders',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 30, 23, 55, 18, 90605, tzinfo=datetime.timezone.utc)),
        ),
    ]
