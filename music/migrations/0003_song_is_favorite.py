# Generated by Django 3.0.7 on 2020-06-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]