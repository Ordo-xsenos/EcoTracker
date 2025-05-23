# Generated by Django 5.1.4 on 2025-05-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchallenge',
            name='challenge',
        ),
        migrations.RemoveField(
            model_name='userchallenge',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='achievement',
            options={'ordering': ['order'], 'verbose_name': 'Достижение', 'verbose_name_plural': 'Достижения'},
        ),
        migrations.RemoveField(
            model_name='achievement',
            name='code',
        ),
        migrations.RemoveField(
            model_name='achievement',
            name='points',
        ),
        migrations.AddField(
            model_name='achievement',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Порядок вывода в списке'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='description',
            field=models.TextField(help_text='Описание достижения'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='icon',
            field=models.CharField(help_text="CSS-класс иконки или emoji, например '🎖️' или имя FontAwesome-класса", max_length=50),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='title',
            field=models.CharField(help_text='Заголовок достижения', max_length=100),
        ),
        migrations.DeleteModel(
            name='Challenge',
        ),
        migrations.DeleteModel(
            name='UserChallenge',
        ),
    ]
