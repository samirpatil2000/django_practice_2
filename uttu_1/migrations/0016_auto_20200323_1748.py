# Generated by Django 3.0.4 on 2020-03-23 17:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uttu_1', '0015_follewer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follewer',
            new_name='Follow',
        ),
    ]