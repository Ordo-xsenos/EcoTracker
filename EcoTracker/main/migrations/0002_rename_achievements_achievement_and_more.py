# Generated by Django 5.1.4 on 2025-05-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Achievements',
            new_name='Achievement',
        ),
        migrations.AddField(
            model_name='userachievement',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
