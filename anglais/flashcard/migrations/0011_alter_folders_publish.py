# Generated by Django 4.1.13 on 2024-05-01 03:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0010_alter_folders_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folders',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 1, 3, 12, 58, 789251, tzinfo=datetime.timezone.utc)),
        ),
    ]