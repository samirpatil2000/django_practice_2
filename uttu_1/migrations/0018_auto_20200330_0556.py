# Generated by Django 3.0.4 on 2020-03-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uttu_1', '0017_playlist_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='name',
            field=models.CharField(default='myPlaylist', max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.TextField(default='mySong', max_length=200),
        ),
    ]
