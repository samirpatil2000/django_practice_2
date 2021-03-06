# Generated by Django 3.0.4 on 2020-09-03 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uttu_1', '0021_author_last_accessed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apk_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='apk_files')),
                ('playStore_link', models.URLField(blank=True)),
                ('title', models.CharField(max_length=40)),
            ],
        ),
    ]
